"""Mock spacecraft telemetry: the speeds of four reaction wheels in a
pyramid during an attitude control test, wheel 3 driven toward saturation.
Replace it with your telemetry client."""
import math


class WheelTelemetry:
    def __init__(self):
        self.k = 0

    def length(self):
        return 200

    def read(self):
        """[wheel speeds in rpm, RW1 to RW4]"""
        t = self.k * 0.5
        self.k += 1
        phases = [0, 1.7, 3.1, 4.4]
        return [3200 * math.sin(t * 0.22 + p) + (2500 * max(0.0, math.sin(t * 0.11)) if w == 2 else 0) + 20 * math.sin(t * 3 + w)
                for w, p in enumerate(phases)]
