"""Mock vector signal analyzer demodulating a 16-QAM carrier while the power
amplifier's bias is tuned: the symbol clouds tighten as the noise falls.
Replace it with your analyzer's driver."""
import random

LEVELS = (-3, -1, 1, 3)


class SignalAnalyzer:
    def __init__(self):
        self.rng = random.Random(11)
        self.k = 0

    def length(self):
        return 110

    def symbols(self, n=16):
        """n received symbols as (I, Q) on the -3..3 grid, and the noise sigma."""
        sigma = max(0.047, 0.6 * 0.955 ** self.k)
        self.k += 1
        out = []
        for _ in range(n):
            i, q = self.rng.choice(LEVELS), self.rng.choice(LEVELS)
            out.append((i + self.rng.gauss(0, sigma), q + self.rng.gauss(0, sigma)))
        return out, sigma
