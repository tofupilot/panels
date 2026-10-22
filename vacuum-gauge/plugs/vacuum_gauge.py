"""Mock vacuum gauge controller: a full-range gauge (PKR) and a Pirani (TPR)
through a chamber pump-down with an outgassing burst when the shroud heats.
Replace it with your gauge controller's driver."""
import math


class VacuumGauge:
    def __init__(self):
        self.k = 0

    def length(self):
        return 200

    def read(self):
        """[PKR pressure in Pa, TPR pressure in Pa or None below its range]"""
        x = min(self.k, 199) / 199
        self.k += 1
        if x < 0.3:
            log_p = 5 - 5 * (1 - math.exp(-4.5 * x / 0.3)) / (1 - math.exp(-4.5))
        else:
            log_p = -4.7 * (1 - math.exp(-4 * (x - 0.3) / 0.7)) / (1 - math.exp(-4))
        if 0.62 < x < 0.8:
            log_p += 1.0 * math.sin(math.pi * (x - 0.62) / 0.18)
        pa = 10 ** (log_p + 0.02 * math.sin(self.k * 1.3))
        return [pa, pa * (1 + 0.04 * math.sin(self.k * 0.4)) if pa >= 5e-2 else None]
