"""Mock chamber thermal programmer: one protoflight cycle of a unit's
baseplate, ramp to -30 °C, 4 h dwell, ramp to +60 °C, 4 h dwell, back to
ambient. Replace it with your controller's driver."""
import math

PROFILE = [("RAMP", 22, -30, 44), ("DWELL", -30, -30, 40), ("RAMP", -30, 60, 52),
           ("DWELL", 60, 60, 40), ("RAMP", 60, 22, 24)]


class ThermalController:
    def __init__(self):
        self.samples = []
        for seg, (kind, t0, t1, steps) in enumerate(PROFILE, start=1):
            for i in range(steps):
                u = (i + 1) / steps
                eased = 0.5 - 0.5 * math.cos(math.pi * u)
                setpoint = t0 if kind == "DWELL" else t0 + (t1 - t0) * eased
                # The baseplate lags the setpoint on a ramp: below it heating, above it cooling.
                pv = setpoint - (1.2 if t1 > t0 else -1.2 if t1 < t0 else 0) * (kind == "RAMP")
                if kind == "DWELL":
                    pv = t0 + (3.1 if t0 > 0 else -1.6) * math.exp(-6 * u) * math.cos(9 * u)
                pv += 0.12 * math.sin(len(self.samples) * 1.9)
                self.samples.append((seg, kind, u, setpoint, pv))
        self.index = 0

    def length(self):
        return len(self.samples)

    def read(self):
        """[program segment, RAMP or DWELL, fraction of the segment, setpoint °C, process value °C]"""
        sample = self.samples[min(self.index, len(self.samples) - 1)]
        self.index += 1
        return list(sample)
