"""Mock pressure-decay leak tester: fills the part to 6 bar, lets it settle,
measures the decay over 10 s, then vents. Replace it with your tester's
driver."""
import math


class LeakTester:
    def __init__(self):
        self.k = 0

    def length(self):
        return 130

    def read(self):
        """[step, gauge pressure in bar, decay in Pa so far]"""
        u = self.k * 0.1
        self.k += 1
        if u < 0.6:
            return ["vented", 0.0, 0.0]
        if u < 3:
            s = (u - 0.6) / 2.4
            bar = 6 * (1 - math.exp(-4 * s)) / (1 - math.exp(-4)) + (0.22 * math.sin(math.pi * s) if s > 0.6 else 0)
            return ["fill", bar, 0.0]
        if u < 6:
            return ["settle", 6 - 0.04 * (1 - math.exp(-(u - 3))), 0.0]
        if u < 11:
            return ["test", 5.96, 2.1 * (u - 6) / 5]
        if u < 12.2:
            return ["vent", 5.96 * (1 - (u - 11) / 1.2), 2.1]
        return ["vented", 0.0, 2.1]
