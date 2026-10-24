"""Mock 4 x 16 crosspoint switch matrix with a multimeter on its analog
buses: ABUS1 goes to the node under test, ABUS2 to ground. Replace it with
your matrix and multimeter drivers."""
import math

NODES = ["VIN", "VBUS", "5V0", "3V3", "1V8", "1V2", "VREF", "VBAT", "AIN0", "AIN1", "AIN2", "AIN3", "NTC", "ISNS", "VCC_IO", "GND"]
LEVELS = [12.012, 5.021, 4.998, 3.2987, 1.8012, 1.2004, 2.4981, 3.2961, 0.4986, 1.0012, 1.4997, 2.0021, 1.6503, 0.1873, 3.3012]


class SwitchMatrix:
    def __init__(self):
        self.closed = set()
        self.k = 0

    def close(self, bus, column):
        self.closed.add((bus, column))

    def open_all(self):
        self.closed.clear()

    def read_dc(self):
        """Volts between ABUS1 and ABUS2."""
        self.k += 1
        node = next((c for b, c in self.closed if b == 0), None)
        return 0.0 if node is None else LEVELS[node] * (1 + 0.00005 * math.sin(self.k * 1.7))
