"""Sweeps the antenna's S11 while its matching network is tuned. `ui.sx*`
and `ui.sy*` are the 41 points of the sweep, real and imaginary parts of the
reflection coefficient, point 20 being 2.45 GHz. The run records the VSWR and
the return loss at 2.45 GHz."""
import math
import time


def match(ui, measurements, vna):
    gamma = 0
    for _ in range(vna.length()):
        sweep = vna.sweep()
        for k, (re, im) in enumerate(sweep):
            setattr(ui, f"sx{k}", round(re, 4))
            setattr(ui, f"sy{k}", round(im, 4))
        gamma = math.hypot(*sweep[20])
        time.sleep(0.4)
    measurements.vswr = round((1 + gamma) / (1 - gamma), 2)
    measurements.return_loss = round(-20 * math.log10(max(gamma, 1e-6)), 1)
    time.sleep(2)
