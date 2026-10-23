"""Switches the supply's three outputs on one after the other and reads them
back. `ui.v1` to `ui.w3` are the readouts, `ui.m1` to `ui.m3` each channel's
mode: CV, CC once its current limit is reached, or OFF. The run records the
VBUS current and the USB1 load current."""
import time

SWITCH_ON = {1: 5, 2: 15, 3: 25}  # read index at which each output comes on


def power_up(ui, measurements, supply):
    for n in range(160):
        for channel, at in SWITCH_ON.items():
            if n == at:
                supply.output(channel, True)
        for channel in (1, 2, 3):
            volts, amps, mode = supply.read(channel)
            setattr(ui, f"v{channel}", f"{volts:.3f}")
            setattr(ui, f"a{channel}", f"{amps:.3f}")
            setattr(ui, f"w{channel}", f"{volts * amps:.3f} W")
            setattr(ui, f"m{channel}", mode)
        time.sleep(0.1)
    measurements.vbus_current = round(supply.read(1)[1], 3)
    measurements.usb1_load_current = round(supply.read(2)[1], 3)
    time.sleep(1.5)
