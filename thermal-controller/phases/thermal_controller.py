"""Runs one protoflight thermal cycle on the chamber programmer. `ui.pv*`
and `ui.sv*` drive the process value and setpoint digits; `ui.op1` and `ui.op2`
light the heat and LN2 outputs, `ui.al1` the deviation alarm past ±2 °C
during a dwell (GEVS temperature tolerance); `ui.prog` names the segment, a
4 h dwell compressed in the replay. The run records each dwell's mean."""
import time


def show(ui, prefix, text):
    """One 7-segment glyph per character, decimal points left to the panel."""
    for k, ch in enumerate(c for c in text if c != "."):
        setattr(ui, f"{prefix}{k}", "_" if ch == " " else ch)

TOLERANCE_C, DWELL_MIN = 2.0, 240


def digits4(c):
    return ("-" if c < 0 else " ") + f"{min(abs(c), 99.9):4.1f}"


def thermal_cycle(ui, measurements, controller):
    dwell = {}
    for _ in range(controller.length()):
        seg, kind, u, setpoint, pv = controller.read()
        show(ui, "pv", digits4(pv))
        show(ui, "sv", digits4(setpoint))
        ui.op1 = setpoint > pv + 0.3
        ui.op2 = setpoint < pv - 0.3
        ui.al1 = kind == "DWELL" and abs(pv - setpoint) > TOLERANCE_C
        if kind == "DWELL":
            minutes = round(u * DWELL_MIN)
            ui.prog = f"SEG {seg} DWELL {minutes // 60}:{minutes % 60:02d} / 4:00"
            dwell.setdefault(setpoint, []).append(pv)
        else:
            ui.prog = f"SEG {seg} RAMP 1.0 °C/min"
        time.sleep(0.1)
    measurements.cold_plateau = round(sum(dwell[-30]) / len(dwell[-30]), 2)
    measurements.hot_plateau = round(sum(dwell[60]) / len(dwell[60]), 2)
    time.sleep(1.5)
