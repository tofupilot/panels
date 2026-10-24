"""Mock vector network analyzer sweeping a 2.4 GHz antenna's S11 from 2.30
to 2.60 GHz while its matching network is tuned. Replace it with your VNA's
driver."""
POINTS = 41
STEPS = 14


def s11(f, f0, r):
    """A series RLC antenna: R ohms at resonance f0, Q of 6, on 50 ohms."""
    x = 6 * r * (f / f0 - f0 / f)
    z = complex(r, x)
    return (z - 50) / (z + 50)


class NetworkAnalyzer:
    def __init__(self):
        self.k = 0

    def length(self):
        return STEPS

    def sweep(self):
        """S11 at POINTS frequencies, as [real, imaginary] pairs."""
        u = min(1.0, self.k / (STEPS - 1))
        self.k += 1
        f0 = 2.37 + 0.08 * (1 - (1 - u) ** 2)
        r = 22 + 27.5 * u
        return [[g.real, g.imag] for g in (s11(2.30 + 0.30 * i / (POINTS - 1), f0, r) for i in range(POINTS))]
