"""Walks the board's functional test, step by step. `ui.step` lights the
parts the step checks on the KiCad drawing and places the label, `ui.tag` is
the label and `ui.ok` turns the highlight red when the check fails. The run
records the 3.3 V regulator's output."""
import time

STEPS = [["regulator", "3.3 V regulator"], ["usb0", "USB0 enumeration"], ["mcu", "MCU"], ["flash", "SPI flash JEDEC ID"], ["usb1", "USB1 power switch"], ["leds", "LEDs"], ["buttons", "Buttons"]]


def functional_test(ui, measurements, board_tester):
    for index, (key, name) in enumerate(STEPS):
        ui.step = index
        passed, readout, value = board_tester.check(key)
        ui.ok = passed
        ui.tag = f"{name}: {readout}"
        if key == "regulator":
            measurements.rail_3v3 = value
        time.sleep(1.8)
    time.sleep(1.5)
