"""Mock pitot-static tester: replays a climb to 6,500 ft, one altitude per
read. Replace it with your air data test set's driver on a real bench."""
import math

# Ground, climb with a small overshoot, settle on the selected altitude.
PROFILE = [(0, 0, 10), (0, 6560, 110), (6560, 6500, 30), (6500, 6500, 25)]


class PitotStaticTester:
    def __init__(self):
        self.samples = []
        for a0, a1, steps in PROFILE:
            for i in range(steps):
                eased = 0.5 - 0.5 * math.cos(math.pi * (i + 1) / steps)
                self.samples.append(a0 + (a1 - a0) * eased + 3 * math.sin(len(self.samples) * 1.7))
        self.index = 0

    def length(self):
        return len(self.samples)

    def read(self):
        """Indicated altitude in ft."""
        alt = self.samples[min(self.index, len(self.samples) - 1)]
        self.index += 1
        return round(alt)
