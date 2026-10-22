"""Mock vibration controller: random vibration at -12, -6, -3 dB and full
level of the GEVS component profile (14.1 Grms at full level). Replace it with
your controller's driver."""
import math
import random

BINS = 36
FREQS = [20 * 100 ** (k / (BINS - 1)) for k in range(BINS)]
LEVELS = [(-12, 40), (-6, 40), (-3, 40), (0, 60), (None, 20)]


def reference(f):
    """GEVS component profile, g²/Hz at full level: +6 dB/oct to 50 Hz,
    0.16 to 800 Hz, -6 dB/oct to 2000 Hz."""
    return 0.16 * (f / 50) ** 2 if f < 50 else 0.16 if f <= 800 else 0.16 * (800 / f) ** 2


class ShakerController:
    def __init__(self):
        self.rng = random.Random(3)
        self.schedule = [level for level, n in LEVELS for _ in range(n)]
        self.k = 0

    def length(self):
        return len(self.schedule)

    def read(self):
        """[level in dB or None when stopped, control ASD in g²/Hz per bin, control Grms]"""
        level = self.schedule[min(self.k, len(self.schedule) - 1)]
        self.k += 1
        if level is None:
            return [None, [], 0.0]
        gain = 10 ** (level / 10)
        asd = [reference(f) * gain * 10 ** ((self.rng.gauss(0, 0.9) + (1.1 if f > 1400 else 0)) / 10) for f in FREQS]
        grms = math.sqrt(sum((asd[k] + asd[k + 1]) / 2 * (FREQS[k + 1] - FREQS[k]) for k in range(BINS - 1)))
        return [level, asd, grms]
