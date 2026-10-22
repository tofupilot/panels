"""Spins a cooling fan up to full duty on an airflow bench. `ui.running`
starts the panel's blade and airflow animations, which loop on their own;
the phase only sends the readings. The run records speed, airflow and noise
once the fan has settled."""
import random
import time


def spin(ui, measurements):
    rng = random.Random(5)
    rpm = 0.0
    ui.running = False
    ui.rpm = 0
    time.sleep(1.0)
    ui.running = True
    for _ in range(120):
        rpm += (3020 - rpm) * 0.06 + rng.uniform(-8, 8)
        ui.rpm = round(rpm)
        ui.airflow = round(rpm / 3020 * 44.5, 1)
        time.sleep(0.08)
    measurements.rpm = round(rpm)
    measurements.airflow = round(rpm / 3020 * 44.5, 1)
    measurements.noise = round(34.8 + rng.uniform(-0.4, 0.4), 1)
    time.sleep(1.5)
    ui.running = False
    time.sleep(1.5)
