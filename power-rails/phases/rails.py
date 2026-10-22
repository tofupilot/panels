"""Probes each rail of a controller board on a bed-of-nails fixture, one
test point at a time. `ui.probe` tells the panel which point the probe is
on; each rail is recorded as a measurement as soon as its reading settles,
so its test point turns green or red on the board drawing right away."""
import random
import time

RAILS = [("vin", 12.02), ("v5", 5.01), ("v3v3", 3.29), ("v1v8", 1.80)]


def probe(ui, measurements):
    rng = random.Random(3)
    ui.probe = "none"
    ui.reading = 0.0
    time.sleep(1.0)
    for key, nominal in RAILS:
        ui.probe = key
        for i in range(20):
            settle = 1 - 0.85 ** (i + 1)
            ui.reading = round(nominal * settle + rng.uniform(-0.01, 0.01), 3)
            time.sleep(0.08)
        setattr(measurements, key, round(nominal + rng.uniform(-0.01, 0.01), 3))
        time.sleep(0.6)
    ui.probe = "shunt"
    for i in range(20):
        ui.reading = round(142 * (1 - 0.8 ** (i + 1)) + rng.uniform(-1, 1), 1)
        time.sleep(0.08)
    measurements.idle_current = round(142 + rng.uniform(-2, 2), 1)
    ui.probe = "done"
    time.sleep(2)
