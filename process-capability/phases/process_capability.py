"""Builds the VBUS histogram board by board. `ui.b*` are the 24 bar counts
from 4.70 to 5.30 V, `ui.f*` the normal fit at 49 points, in the same counts.
The run records the Cpk against the 4.75-5.25 V limits and the mean."""
import math
import statistics
import time

LOW, HIGH, LSL, USL, BINS = 4.70, 5.30, 4.75, 5.25, 24


def process_capability(ui, measurements, production_line):
    values, counts = [], [0] * BINS
    width = (HIGH - LOW) / BINS
    for n in range(120):
        for _ in range(2):
            v = production_line.next_unit()
            values.append(v)
            k = int((v - LOW) / width)
            if 0 <= k < BINS:
                counts[k] += 1
                setattr(ui, f"b{k}", counts[k])
        if len(values) > 5:
            mean, sd = statistics.mean(values), statistics.stdev(values)
            for k in range(49):
                x = LOW + k * (HIGH - LOW) / 48
                density = math.exp(-((x - mean) / sd) ** 2 / 2) / (sd * math.sqrt(2 * math.pi))
                setattr(ui, f"f{k}", round(density * len(values) * width, 2))
        time.sleep(0.1)
    mean, sd = statistics.mean(values), statistics.stdev(values)
    measurements.cpk = round(min(USL - mean, mean - LSL) / (3 * sd), 2)
    measurements.mean = round(mean, 4)
    time.sleep(1.5)
