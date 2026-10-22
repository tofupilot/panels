"""Mock rate table: replays a right standard-rate turn, one turn rate and
slip per read. Replace it with your rate table's driver on a real bench."""
import math

# Level, roll into the turn, hold it, roll out, level.
PROFILE = [(0, 0, 10), (0, 3.0, 25), (3.0, 3.0, 50), (3.0, 0, 25), (0, 0, 15)]


class RateTable:
    def __init__(self):
        self.samples = []
        for r0, r1, steps in PROFILE:
            for i in range(steps):
                eased = 0.5 - 0.5 * math.cos(math.pi * (i + 1) / steps)
                rate = r0 + (r1 - r0) * eased + 0.03 * math.sin(len(self.samples) * 1.9)
                # The ball skids out while the rate changes, then centers.
                slip = 0.35 * (r1 - r0) * math.sin(math.pi * (i + 1) / steps)
                self.samples.append((rate, slip))
        self.index = 0
        self.turn = range(35, 85)

    def length(self):
        return len(self.samples)

    def in_turn(self):
        """Whether the last read was in the steady part of the turn."""
        return self.index - 1 in self.turn

    def read(self):
        """[turn rate in degrees per second, slip in ball widths]"""
        rate, slip = self.samples[min(self.index, len(self.samples) - 1)]
        self.index += 1
        return [round(rate, 2), round(slip, 2)]
