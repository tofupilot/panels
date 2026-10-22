"""Runs one thermal vacuum cycle. The panel's tape follows `ui.temp`, puts
the GEVS ±2 °C band on `ui.target`, and turns amber with `ui.cycle_state`
when the baseplate leaves the band during a dwell. `ui.stage` shows the step
and the dwell time, a 4 h plateau compressed in the replay. The run records
the mean baseplate temperature of each dwell."""
import time

TOLERANCE_C = 2.0
DWELL_HOURS = 4


def thermal_cycle(ui, measurements, controller):
    dwell = {"COLD DWELL": [], "HOT DWELL": []}
    for _ in range(controller.length()):
        stage, setpoint, i, steps, temp = controller.read()
        ui.temp = round(temp, 1)
        ui.target = setpoint if setpoint is not None else "none"
        if setpoint is None:
            ui.stage = stage
            ui.cycle_state = "ok"
        else:
            minutes = round((i + 1) / steps * DWELL_HOURS * 60)
            ui.stage = f"{stage} {minutes // 60}:{minutes % 60:02d} / {DWELL_HOURS}:00"
            ui.cycle_state = "warn" if abs(temp - setpoint) > TOLERANCE_C else "ok"
            dwell[stage].append(temp)
        time.sleep(0.1)
    measurements.cold_plateau = round(sum(dwell["COLD DWELL"]) / len(dwell["COLD DWELL"]), 2)
    measurements.hot_plateau = round(sum(dwell["HOT DWELL"]) / len(dwell["HOT DWELL"]), 2)
    time.sleep(1.5)
