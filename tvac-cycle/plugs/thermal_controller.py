"""Mock thermal controller: replays one protoflight thermal vacuum cycle of a
unit's baseplate, ambient to a -30 °C cold plateau, to a +60 °C hot plateau
and back, one reading per call. Replace it with your chamber controller's
driver on a real bench."""
import math

# (stage, from °C, to °C, samples): ramps at most 1 °C/min on the real chamber.
PROFILE = [("RAMP COLD", 22, -30, 40), ("COLD DWELL", -30, -30, 35), ("RAMP HOT", -30, 60, 55),
           ("HOT DWELL", 60, 60, 35), ("RAMP AMBIENT", 60, 22, 35)]


class ThermalController:
    def __init__(self):
        self.samples = []
        for stage, t0, t1, steps in PROFILE:
            for i in range(steps):
                x = (i + 1) / steps
                temp = t0 + (t1 - t0) * (0.5 - 0.5 * math.cos(math.pi * x))
                if stage.endswith("DWELL"):
                    # the controller overshoots, then settles into the band
                    temp = t0 + (2.9 if t0 > 0 else -1.4) * math.exp(-6 * x) * math.cos(9 * x)
                self.samples.append((stage, t1 if stage.endswith("DWELL") else None, i, steps, temp + 0.15 * math.sin(len(self.samples) * 1.7)))
        self.index = 0

    def length(self):
        return len(self.samples)

    def read(self):
        """[stage, plateau setpoint in °C or None, sample in stage, samples in stage, baseplate °C]"""
        sample = self.samples[min(self.index, len(self.samples) - 1)]
        self.index += 1
        return list(sample)
