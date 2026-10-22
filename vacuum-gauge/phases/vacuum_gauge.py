"""Pumps the thermal vacuum chamber down and reads the gauge controller.
`ui.c1_*` and `ui.c2_*` drive the two channels' digits in E-notation, the
Pirani showing Ur below its range; `ui.sp1` and `ui.sp2` light the setpoint
relays at 10 Pa and at 1.33e-3 Pa, the test vacuum of NASA GEVS. The run
records the pressure at the end of pump-down."""
import math
import time


def show(ui, prefix, text):
    """One 7-segment glyph per character, decimal points left to the panel."""
    for k, ch in enumerate(c for c in text if c != "."):
        setattr(ui, f"{prefix}{k}", "_" if ch == " " else ch)

SP1_PA, SP2_PA = 10.0, 1.33e-3


def e_notation(pa):
    exponent = math.floor(math.log10(pa))
    mantissa = pa / 10 ** exponent
    if round(mantissa, 1) >= 10:
        mantissa, exponent = mantissa / 10, exponent + 1
    return f"{mantissa:3.1f}E{'-' if exponent < 0 else ' '}{abs(exponent):02d}"


def pump_down(ui, measurements, gauge):
    pa = 1e5
    for _ in range(gauge.length()):
        pa, pirani = gauge.read()
        show(ui, "c1_", e_notation(pa))
        if pirani is None:
            show(ui, "c2_", " Ur   ")
            ui.c2dp = False
        else:
            show(ui, "c2_", e_notation(pirani))
            ui.c2dp = True
        ui.sp1 = pa < SP1_PA
        ui.sp2 = pa < SP2_PA
        time.sleep(0.1)
    measurements.test_pressure = float(f"{pa:.3g}")
    time.sleep(1.5)
