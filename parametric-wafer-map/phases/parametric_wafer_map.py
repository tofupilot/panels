"""Measures each die's threshold voltage touchdown by touchdown and uncovers it
on the wafer's heat map (`ui.td`, a count). The run records the mean
threshold voltage and its spread."""
import statistics
import time


def measure_vth(ui, measurements, parametric_tester):
    values = []
    for k in range(parametric_tester.touchdowns()):
        values += [v for v in parametric_tester.touchdown() if v is not None]
        ui.td = k
        time.sleep(0.1)
    measurements.vth_mean = round(statistics.mean(values), 2)
    measurements.vth_sigma = round(statistics.pstdev(values), 2)
    time.sleep(1.5)
