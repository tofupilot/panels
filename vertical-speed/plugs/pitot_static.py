"""Mock pitot-static tester: replays a climb and a steep descent, one
vertical speed per read. Replace it with your air data test set's driver on
a real bench."""
import math

# Level, climb at 1,000 fpm, level, a steep descent, recover, level.
PROFILE = [("level", 0, 0, 10), ("enter", 0, 1000, 25), ("climb", 1000, 1000, 40), ("level", 1000, 0, 20),
           ("descent", 0, -1700, 25), ("descent", -1700, -700, 20), ("level", -700, 0, 20)]


class PitotStaticTester:
    def __init__(self):
        self.samples = []
        for segment, v0, v1, steps in PROFILE:
            for i in range(steps):
                eased = 0.5 - 0.5 * math.cos(math.pi * (i + 1) / steps)
                self.samples.append((segment, v0 + (v1 - v0) * eased + 8 * math.sin(len(self.samples) * 1.7)))
        self.index = 0

    def length(self):
        return len(self.samples)

    def read(self):
        """[flight segment, vertical speed in fpm, climb positive]"""
        segment, fpm = self.samples[min(self.index, len(self.samples) - 1)]
        self.index += 1
        return [segment, round(fpm)]
