"""Mock digital force gauge on a motorised test stand pushing a connector
into its header: spring rise, the latch peak near 2.9 mm, the drop past the
latch, then seated. Replace it with your gauge's driver."""
import math


def insertion(mm):
    if mm < 2.9:
        return 23.6 * (mm / 2.9) ** 1.6
    if mm < 3.3:
        return 23.6 - (mm - 2.9) / 0.4 * 15.2
    return 8.4 + max(0.0, mm - 5.4) * 60


class ForceGauge:
    def __init__(self):
        self.k = 0

    def read(self, mm):
        """Force in N at a stand position in mm."""
        self.k += 1
        return insertion(mm) + 0.12 * math.sin(self.k * 1.4)
