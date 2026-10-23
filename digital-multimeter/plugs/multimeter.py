"""Mock 6 1/2-digit multimeter behind a scanner card, reading the GreatFET
One's rails on channels 101 to 104. Replace it with your multimeter's driver
(SCPI: ROUT:CLOS (@101), then MEAS:VOLT:DC? 10)."""
import math

RAILS = {101: 5.0213, 102: 3.2987, 103: 5.0105, 104: 3.2961}


class Multimeter:
    def __init__(self):
        self.k = 0

    def read_dc(self, channel):
        """Volts on a scanner channel, 10 V range."""
        self.k += 1
        return RAILS[channel] * (1 + 0.00004 * math.sin(self.k * 0.7) + 0.00002 * math.sin(self.k * 2.3))
