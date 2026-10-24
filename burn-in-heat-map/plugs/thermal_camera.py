"""Mock thermal camera above a board in burn-in: a 12 x 9 grid of
temperatures over the GreatFET One, the MCU (U1) and the 3.3 V regulator (U3)
heating up. Replace it with your camera's driver."""
import math

COLS, ROWS = 12, 9
HOT = [(368, 302, 34.7, 120), (101, 183, 17.0, 70)]  # board units (0.1 mm): x, y, rise in C, spread


class ThermalCamera:
    def __init__(self):
        self.k = 0

    def length(self):
        return 34

    def frame(self):
        """Temperatures in C, row by row, after another 30 s of burn-in."""
        rise = 1 - math.exp(-self.k / 9)
        self.k += 1
        out = []
        for r in range(ROWS):
            for c in range(COLS):
                x, y = (c + 0.5) * 716 / COLS, (r + 0.5) * 543 / ROWS
                t = 25 + 3.0 * rise
                for hx, hy, amp, s in HOT:
                    t += rise * amp * math.exp(-((x - hx) ** 2 + (y - hy) ** 2) / (2 * s * s))
                out.append(t)
        return out
