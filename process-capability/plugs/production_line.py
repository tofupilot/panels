"""Mock production line: the VBUS rail measured on each board as it passes
the functional test, normally distributed around 5.011 V. Replace it with
your own measurement source."""
import random


class ProductionLine:
    def __init__(self):
        self.rng = random.Random(23)

    def next_unit(self):
        """The VBUS rail of the next board, in volts."""
        return self.rng.gauss(5.011, 0.047)
