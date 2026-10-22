"""Mock bus power supply: replays a unit switched on from a 28 V supply,
the inrush at switch-on, then load steps as its modes start, one reading per
call. Replace it with your power supply's driver on a real bench."""
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
        inrush = 2.6 * math.exp(-t / 2.5) if t < 15 else 0.0
        amps = load + inrush + 0.02 * math.sin(k * 1.9)
        volts = 28.05 - 0.35 * amps + 0.03 * math.sin(k * 1.3)
        return [round(volts, 3), round(amps, 3)]
