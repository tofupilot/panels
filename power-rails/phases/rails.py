"""Probes each rail of a controller board on a bed-of-nails fixture, one
test point at a time. `ui.probe` tells the panel which point the probe is
on; each rail is recorded as a measurement as soon as its reading settles,
so its test point turns green or red on the board drawing right away."""
import time

RAILS = ["vin", "v5", "v3v3", "v1v8"]


def probe(ui, measurements, dmm):
    ui.probe = "none"
    ui.reading = 0.0
    time.sleep(1.0)
    for rail in RAILS + ["shunt"]:
        ui.probe = rail
        dmm.move_to(rail)
        for _ in range(20):
            reading = dmm.read()
            ui.reading = reading
            time.sleep(0.08)
        if rail == "shunt":
            measurements.idle_current = round(reading, 1)
        else:
            setattr(measurements, rail, reading)
        time.sleep(0.6)
    ui.probe = "done"
    time.sleep(2)
