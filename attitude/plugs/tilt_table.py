"""Mock tilt table: replays a short maneuver, one pitch and roll per read.
Replace it with your tilt table's driver on a real bench."""
import math

# Level, pitch up, bank right, hold the turn, roll out, pitch down, level.
PROFILE = [((0, 0), (0, 0), 10), ((0, 0), (8, 0), 20), ((8, 0), (8, 20), 25), ((8, 20), (8, 20), 30),
           ((8, 20), (8, 0), 25), ((8, 0), (0, 0), 20), ((0, 0), (0, 0), 20)]


class TiltTable:
    def __init__(self):
        self.samples = []
        for (p0, r0), (p1, r1), steps in PROFILE:
            for i in range(steps):
                eased = 0.5 - 0.5 * math.cos(math.pi * (i + 1) / steps)
                wobble = 0.15 * math.sin(len(self.samples) * 1.3)
                self.samples.append((p0 + (p1 - p0) * eased + wobble, r0 + (r1 - r0) * eased - wobble))
        self.index = 0

    def length(self):
        return len(self.samples)

    def read(self):
        """[pitch in degrees, roll in degrees, right wing down positive]"""
        pitch, roll = self.samples[min(self.index, len(self.samples) - 1)]
        self.index += 1
        return [round(pitch, 2), round(roll, 2)]
