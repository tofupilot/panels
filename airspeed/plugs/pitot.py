"""Mock pitot probe: replays a short flight, one indicated airspeed per read.
Replace it with your air data test set's driver on a real bench."""
import math

# Takeoff roll, climb, level off, an overspeed in the descent, then cruise.
PROFILE = [(0, 65, 40), (65, 95, 30), (95, 140, 30), (140, 172, 25), (172, 124, 30)]


class PitotProbe:
    def __init__(self):
        self.samples = []
        for v0, v1, steps in PROFILE:
            for i in range(steps + 1):
                eased = 0.5 - 0.5 * math.cos(math.pi * i / steps)
                self.samples.append(v0 + (v1 - v0) * eased + 0.6 * math.sin(i * 1.7))
        self.index = 0

    def length(self):
        return len(self.samples)

    def read(self):
        """Indicated airspeed in kt."""
        ias = self.samples[min(self.index, len(self.samples) - 1)]
        self.index += 1
        return round(ias, 1)
