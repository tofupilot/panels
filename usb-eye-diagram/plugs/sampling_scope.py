"""Mock oscilloscope folding a USB 2.0 high-speed data line into an eye:
480 Mb/s, +/-400 mV levels, a 0.24 UI rise time, random jitter and noise.
Replace it with your scope's driver."""
import math
import random

POINTS = 40


class SamplingScope:
    def __init__(self):
        self.rng = random.Random(7)

    def trace(self):
        """One 2-UI window, -0.5 to 1.5 UI, in mV."""
        b = [self.rng.choice((-400, 400)) for _ in range(3)]
        j0, j1 = self.rng.gauss(0, 0.025), self.rng.gauss(0, 0.025)
        out = []
        for k in range(POINTS):
            t = -0.5 + 2 * k / (POINTS - 1)
            v = b[0]
            for edge, (a, c) in ((j0, (b[0], b[1])), (1 + j1, (b[1], b[2]))):
                u = (t - edge) / 0.24 + 0.5
                if u >= 1:
                    v = c
                elif u > 0:
                    v = a + (c - a) * (0.5 - 0.5 * math.cos(math.pi * u))
            out.append(v + self.rng.gauss(0, 12))
        return out
