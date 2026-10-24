"""Mock LED analyzer: a fiber over each of the board's eight LEDs, returning
the CIE 1931 chromaticity and the intensity of the one lit. Replace it with
your analyzer's driver."""

LEDS = [
    (0.6950, 0.3046, 182), (0.6938, 0.3058, 176), (0.1689, 0.7212, 410), (0.1702, 0.7189, 398),
    (0.1305, 0.0752, 96), (0.1312, 0.0731, 101), (0.5701, 0.4269, 140), (0.3290, 0.3420, 1120),
]


class LedAnalyzer:
    def measure(self, index):
        """[x, y, intensity in mcd] of LED D1..D8 (index 0..7)."""
        return list(LEDS[index])
