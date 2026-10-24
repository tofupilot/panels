"""Reads the product's supply current while its stages switch on and shows it
on the moving-coil ammeter: `ui.amps` turns the needle. The run records the
standby current and the full-load current."""
import time


def supply_current(ui, measurements, load_ammeter):
    for _ in range(load_ammeter.length()):
        stage, amps = load_ammeter.read()
        ui.amps = round(amps, 2)
        if stage == 2:
            standby = amps
        if stage == 6:
            load = amps
        time.sleep(0.1)
    measurements.standby_current = standby
    measurements.load_current = load
    time.sleep(1.5)
