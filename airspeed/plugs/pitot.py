"""Mock pitot probe: replays a short flight, one indicated airspeed per read.
Replace it with your air data test set's driver on a real bench."""
import math

PROFILE = [
    ("Takeoff roll", 0, 65, 40),
    ("Rotate and climb", 65, 95, 30),
    ("Level off, accelerate", 95, 140, 30),
    ("Descent: overspeed!", 140, 172, 25),
    ("Power back, cruise", 172, 118, 30),
]


class PitotProbe:
    def __init__(self):
        self.offset = 6.0
        self.samples = []
        for label, v0, v1, steps in PROFILE:
            for i in range(steps + 1):
                eased = 0.5 - 0.5 * math.cos(math.pi * i / steps)
                self.samples.append((label, v0 + (v1 - v0) * eased + 0.6 * math.sin(i * 1.7)))
        self.index = 0

    def length(self):
        return len(self.samples)

    def zero(self):
        self.offset = 0.0

    def read(self):
        """[flight segment, indicated airspeed in kt, probe offset in kt]"""
        label, ias = self.samples[min(self.index, len(self.samples) - 1)]
        self.index += 1
        return [label, round(ias + self.offset, 1), self.offset]
