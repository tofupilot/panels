"""Pumps the thermal vacuum chamber down. The panel's log tape follows
`ui.decades` (decades below atmosphere), shows `ui.pressure` with its power
of ten, and turns green with `ui.at_vacuum` below 1.33e-3 Pa, the test
vacuum of NASA GEVS. The run records the pressure at the end of pump-down."""
import math
import time

TEST_VACUUM_PA = 1.33e-3
SUPERSCRIPT = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")


def sci(pa):
    exponent = math.floor(math.log10(pa))
    return f"{pa / 10 ** exponent:.1f} × 10{str(exponent).translate(SUPERSCRIPT)}"


def pump_down(ui, measurements, gauge):
    pa = 1e5
    for _ in range(gauge.length()):
        pa = gauge.read()
        ui.pressure = sci(pa)
        ui.decades = round(5 - math.log10(pa), 3)
        ui.at_vacuum = pa < TEST_VACUUM_PA
        ui.regime = "ROUGHING" if pa > 1 else "TEST VACUUM" if pa < TEST_VACUUM_PA else "TURBO"
        time.sleep(0.1)
    measurements.test_pressure = float(f"{pa:.3g}")
    time.sleep(1.5)
