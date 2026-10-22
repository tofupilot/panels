"""Spins the fan up to full duty. `ui.running` starts the panel's blade and
airflow animations, which loop on their own; the phase only sends the
readings. The run records speed, airflow and noise once the fan has settled."""
import time


def spin(ui, measurements, bench):
    ui.running = False
    ui.rpm = 0
    time.sleep(1.0)
    bench.start()
    ui.running = True
    for _ in range(120):
        rpm, airflow = bench.read()
        ui.rpm, ui.airflow = rpm, airflow
        time.sleep(0.08)
    measurements.rpm = rpm
    measurements.airflow = airflow
    measurements.noise = bench.noise()
    time.sleep(1.5)
    bench.stop()
    ui.running = False
    time.sleep(1.5)
