"""Mock triple-output supply: CH1 is VBUS into the board's USB0, CH2 feeds an
electronic load on its USB1 host port, CH3 an external target whose current
limit is set too low. Replace it with your supply's driver."""
import math

CHANNELS = [  # set volts, current limit, load ohms
    (5.0, 0.5, 42.0),
    (5.0, 0.6, 10.0),
    (3.3, 0.1, 10.2),
]


class TripleSupply:
    def __init__(self):
        self.k = 0
        self.on = [False, False, False]

    def output(self, channel, on):
        self.on[channel - 1] = on

    def read(self, channel):
        """[volts, amps, 'CV' | 'CC' | 'OFF'] of one channel."""
        self.k += 1
        if not self.on[channel - 1]:
            return [0.0, 0.0, "OFF"]
        vset, ilim, load = CHANNELS[channel - 1]
        wobble = math.sin(self.k * 0.37 + channel)
        if vset / load > ilim:
            return [ilim * load * (1 + 0.0002 * wobble), ilim * (1 + 0.002 * wobble), "CC"]
        return [vset * (1 + 0.0002 * wobble), vset / load * (1 + 0.002 * wobble), "CV"]
