"""Mock two-pen chart recorder on a climatic chamber running a cold soak at
-40 C, then a damp-heat dwell at +85 C / 85 %RH (IEC 60068-2-30 style,
compressed), then recovery. Replace it with your recorder's or chamber's driver."""
import math

PROFILE = [(0.00, 23, 45), (0.12, -40, 0), (0.34, -40, 0), (0.50, 85, 85), (0.86, 85, 85), (1.00, 23, 45)]


def _ease(x):
    return 0.5 - 0.5 * math.cos(math.pi * min(1.0, max(0.0, x)))


class ChartRecorder:
    def __init__(self):
        self.k = 0

    def length(self):
        return 250

    def read(self):
        """[temperature in C, relative humidity in %RH, True during the damp-heat dwell]"""
        x = self.k / (self.length() - 1)
        self.k += 1
        for (x0, t0, h0), (x1, t1, h1) in zip(PROFILE, PROFILE[1:]):
            if x <= x1:
                u = _ease((x - x0) / (x1 - x0))
                temp, rh = t0 + (t1 - t0) * u, h0 + (h1 - h0) * u
                break
        temp += 0.25 * math.sin(self.k * 0.11)
        rh += 0.8 * math.sin(self.k * 0.077) if rh > 1 else 0
        return [temp, rh, 0.55 <= x <= 0.84]
