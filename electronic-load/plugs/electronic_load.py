"""Mock DC electronic load discharging a 12 V, 7.2 Ah lead-acid battery at C/10
(0.72 A) in constant current until the 10.5 V cutoff, ten hours compressed into
the replay. Replace it with your load's driver."""
import math

CAPACITY_AH = 7.38


class ElectronicLoad:
    def __init__(self):
        self.k = 0

    def length(self):
        return 160

    def read(self):
        """[volts, amps, amp-hours, seconds, input on]"""
        q = min(1.0, self.k / 130)
        self.k += 1
        on = self.k <= 131
        if q < 0.02:
            v = 12.6 - q / 0.02 * 0.35
        elif q < 0.85:
            v = 12.25 - (q - 0.02) * 0.82
        else:
            v = 11.57 - ((q - 0.85) / 0.17) ** 2.2 * 1.07
        if not on:
            v = 11.9 + 0.5 * (1 - math.exp(-(self.k - 131) / 6))
        v += 0.0006 * math.sin(self.k * 0.9)
        amps = 0.72 + 0.0002 * math.sin(self.k * 1.3) if on else 0.0
        ah = q * CAPACITY_AH
        return [v, amps, ah, ah / 0.72 * 3600, on]
