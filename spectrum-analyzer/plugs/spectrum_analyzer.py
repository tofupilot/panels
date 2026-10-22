"""Mock spectrum analyzer on the S-band downlink: the noise floor, then the
QPSK carrier rising as the transmitter warms and the coupler is set. Replace it
with your analyzer's driver."""
import math
import random

POINTS, SPAN_MHZ, CENTER_MHZ = 48, 2.0, 2245.0


class SpectrumAnalyzer:
    def __init__(self):
        self.k = 0
        self.rng = random.Random(7)
        self.trace = [-95.0] * POINTS

    def length(self):
        return 200

    def sweep(self):
        """[trace in dBm, one point per bin across the span]"""
        x = self.k / 199
        self.k += 1
        level = -120.0 if x < 0.12 else -78 + 32 * (0.5 - 0.5 * math.cos(math.pi * min(1, (x - 0.12) / 0.5)))
        for b in range(POINTS):
            u = ((b / (POINTS - 1)) - 0.5) * SPAN_MHZ / 0.45
            sinc = 1.0 if abs(u) < 1e-6 else (math.sin(math.pi * u) / (math.pi * u)) ** 2
            p = 10 * math.log10(10 ** (-9.6) + 10 ** ((level + 10 * math.log10(sinc + 1e-6)) / 10)) + self.rng.gauss(0, 1.3)
            self.trace[b] = self.trace[b] * 0.6 + p * 0.4
        return list(self.trace)
