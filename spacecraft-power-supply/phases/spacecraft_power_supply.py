"""Switches the spacecraft on from the EGSE supply on its 28 V bus. `ui.v*`
and `ui.i*` drive the display, `ui.cv` and `ui.cc` the regulation mode,
`ui.limit` lights outside the 22-36 V bus input range. The run records the
lowest bus voltage under load and the steady-state current."""
import time


def show(ui, prefix, text):
    """One 7-segment glyph per character, decimal points left to the panel."""
    for k, ch in enumerate(c for c in text if c != "."):
        setattr(ui, f"{prefix}{k}", "_" if ch == " " else ch)

INPUT_RANGE_V = (22.0, 36.0)


def power_on(ui, measurements, supply):
    low, last = 99.0, 0.0
    for n in range(supply.length()):
        volts, amps = supply.read()
        show(ui, "v", f"{volts:5.2f}")
        show(ui, "i", f"{amps:5.3f}")
        on = volts > 1
        ui.out = on
        ui.cv = on and amps < 3
        ui.cc = amps >= 3
        ui.limit = on and n > 15 and not INPUT_RANGE_V[0] <= volts <= INPUT_RANGE_V[1]
        if amps > 0.1:
            low, last = min(low, volts), amps
        time.sleep(0.1)
    measurements.bus_voltage = round(low, 2)
    measurements.steady_current = round(last, 2)
    time.sleep(1.5)
