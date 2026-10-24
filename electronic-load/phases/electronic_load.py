"""Discharges the battery through the electronic load at C/10 to the 10.5 V
cutoff. `ui.v`, `ui.a`, `ui.w`, `ui.ah` and `ui.time` drive the display. The
run records the capacity delivered."""
import time


def discharge(ui, measurements, electronic_load):
    capacity = 0.0
    for _ in range(electronic_load.length()):
        volts, amps, ah, seconds, on = electronic_load.read()
        ui.v = f"{volts:.4f}"
        ui.a = f"{amps:.4f}"
        ui.w = f"{volts * amps:.3f} W"
        ui.ah = f"{ah:.3f} Ah"
        s = int(seconds)
        ui.time = f"{s // 3600:02d}:{s // 60 % 60:02d}:{s % 60:02d}"
        capacity = ah
        time.sleep(0.1)
    measurements.capacity = round(capacity, 2)
    time.sleep(1.5)
