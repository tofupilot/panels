"""Mock turntable: replays a right turn from 090 to 270, one heading per read.
Replace it with your turntable's driver on a real bench."""
import math

# Hold, turn right with a small overshoot, settle on the selected heading.
PROFILE = [(90, 90, 10), (90, 272, 110), (272, 270, 30), (270, 270, 25)]


class Turntable:
    def __init__(self):
        self.samples = []
        for h0, h1, steps in PROFILE:
            for i in range(steps):
                eased = 0.5 - 0.5 * math.cos(math.pi * (i + 1) / steps)
                self.samples.append(h0 + (h1 - h0) * eased + 0.2 * math.sin(len(self.samples) * 1.7))
        self.index = 0

    def length(self):
        return len(self.samples)

    def read(self):
        """Heading in degrees."""
        heading = self.samples[min(self.index, len(self.samples) - 1)]
        self.index += 1
        return round(heading, 1)
