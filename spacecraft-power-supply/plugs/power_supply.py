"""Mock EGSE power supply on the spacecraft's 28 V bus: switch-on, the
inrush, then load steps as subsystems power up. Replace it with your supply's
driver."""
import math


class PowerSupply:
    def __init__(self):
        self.k = 0

    def length(self):
        return 180

    def read(self):
        """[bus voltage in V, current in A]"""
        k = self.k
        self.k += 1
        if k < 15:
            return [0.0 if k < 10 else 28.0 * (k - 9) / 5, 0.0]
        t = k - 15
        load = 0.62 + (0.35 if t > 50 else 0) + (0.18 if t > 110 else 0)
        amps = load + (2.6 * math.exp(-t / 2.5) if t < 15 else 0.0) + 0.02 * math.sin(k * 1.9)
        return [28.05 - 0.35 * amps + 0.03 * math.sin(k * 1.3), amps]
