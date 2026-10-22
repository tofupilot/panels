"""Mock vacuum gauge: replays a chamber pump-down, roughing pump then turbo
pump, with an outgassing burst when the shroud heats, one reading per call.
Replace it with your chamber gauge's driver on a real bench."""
import math


class VacuumGauge:
    def __init__(self):
        self.k = 0

    def length(self):
        return 200

    def read(self):
        """Chamber pressure in Pa."""
        x = min(self.k, 199) / 199
        self.k += 1
        if x < 0.3:            # roughing pump: atmosphere to 1 Pa
            log_p = 5.0 - 5.0 * (1 - math.exp(-4.5 * x / 0.3)) / (1 - math.exp(-4.5))
        else:                  # turbo pump: down to the 1e-5 Pa decade
            log_p = 0.0 - 4.6 * (1 - math.exp(-4.0 * (x - 0.3) / 0.7)) / (1 - math.exp(-4.0))
        if 0.62 < x < 0.78:    # outgassing when the shroud heats
            log_p += 0.9 * math.sin(math.pi * (x - 0.62) / 0.16)
        return 10 ** (log_p + 0.03 * math.sin(self.k * 1.3))
