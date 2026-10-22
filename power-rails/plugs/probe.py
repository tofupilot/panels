"""Mock flying probe and DMM on a controller board: moves to a test point,
then reads a value that settles like a real meter. Replace it with your
fixture's probe and DMM drivers on a real bench."""
import random

NOMINAL = {"vin": 12.02, "v5": 5.01, "v3v3": 3.29, "v1v8": 1.80, "shunt": 142.0}


class Probe:
    def __init__(self):
        self.rng = random.Random(3)
        self.point, self.samples = None, 0

    def move_to(self, point):
        self.point, self.samples = point, 0

    def read(self):
        """The meter's reading on the current test point: volts, or mA on the shunt."""
        nominal = NOMINAL[self.point]
        self.samples += 1
        settle = 1 - 0.7 ** self.samples
        noise = 1.0 if self.point == "shunt" else 0.01
        return round(nominal * settle + self.rng.uniform(-noise, noise), 3)
