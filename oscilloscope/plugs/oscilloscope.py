"""Mock 4-channel oscilloscope capturing the GreatFET One's power-up on a
single trigger: VBUS, the 3.3 V regulator, nRESET and LED1. Replace it with
your scope's driver (SINGle, then WAVeform:DATA? per channel)."""
import math
import random

POINTS = 75
TRACES = [  # volts, start in divisions, time constant in divisions
    (5.0, 1.0, 0.12),
    (3.3, 1.6, 0.30),
    (3.3, 3.7, 0.05),
    (3.3, 7.2, 0.03),
]


class Oscilloscope:
    def __init__(self):
        self.rng = random.Random(5)

    def single(self):
        """Four traces of POINTS samples over 10 divisions at 1 ms/div, in volts."""
        out = []
        for v, t0, tau in TRACES:
            trace = []
            for k in range(POINTS):
                x = k / (POINTS - 1) * 10
                level = 0.0 if x < t0 else v * (1 - math.exp(-(x - t0) / tau))
                trace.append(level + self.rng.gauss(0, 0.02))
            out.append(trace)
        return out
