"""Mock audio analyzer reading an amplifier's two outputs while a 1 kHz tone
steps up to the +4 dBu nominal level. Replace it with your analyzer's driver."""
import math

STEPS = [-30, -20, -10, 0, 4, 4, 4]


class AudioAnalyzer:
    def __init__(self):
        self.k = 0

    def length(self):
        return 91

    def read(self):
        """[left dBu, right dBu]"""
        step = STEPS[min(len(STEPS) - 1, self.k * len(STEPS) // self.length())]
        self.k += 1
        return [step + 0.05 + 0.15 * math.sin(self.k * 0.43), step - 0.12 + 0.15 * math.sin(self.k * 0.38 + 1)]
