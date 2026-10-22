"""Mock shaker controller: replays a random vibration run at -12, -6, -3 dB
and full level, one control Grms reading per call. Full level is 14.1 Grms,
the GEVS component example. Replace it with your vibration controller's
driver on a real bench."""
import math

FULL_LEVEL_GRMS = 14.1
LEVELS = [(-12, 35), (-6, 35), (-3, 40), (0, 70), (None, 20)]


class ShakerController:
    def __init__(self):
        self.samples = []
        for level, steps in LEVELS:
            for i in range(steps):
                if level is None:
                    self.samples.append((None, 0.0, max(0.0, 1.2 * (1 - (i + 1) / 6))))
                    continue
                reference = FULL_LEVEL_GRMS * 10 ** (level / 20)
                settle = 1 - math.exp(-(i + 1) / 3)
                noise = 0.03 * math.sin(len(self.samples) * 2.1) + 0.02 * math.sin(len(self.samples) * 5.3)
                self.samples.append((level, reference, reference * settle * (1 + noise)))
        self.index = 0

    def length(self):
        return len(self.samples)

    def read(self):
        """[level in dB or None when stopped, reference Grms, control Grms]"""
        sample = self.samples[min(self.index, len(self.samples) - 1)]
        self.index += 1
        return list(sample)
