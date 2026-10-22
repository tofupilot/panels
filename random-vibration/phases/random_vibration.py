"""Runs random vibration at -12, -6, -3 dB and full level of the GEVS
component profile. `ui.level` shows that level's reference, tolerance and
abort lines; `ui.p0` to `ui.p35` are the control ASD (log10 g²/Hz) and
`ui.grms` the control Grms. The run records the mean Grms at full level."""
import math
import time


def random_vibration(ui, measurements, shaker):
    full = []
    for n in range(shaker.length()):
        level, asd, grms = shaker.read()
        ui.level = "stop" if level is None else str(level)
        if level is None:
            ui.grms = "STOPPED"
        elif n % 2 == 0:
            for k, g in enumerate(asd):
                setattr(ui, f"p{k}", round(math.log10(g), 3))
            ui.grms = f"{grms:.2f} Grms"
        if level == 0:
            full.append(grms)
        time.sleep(0.1)
    measurements.full_level_grms = round(sum(full) / len(full), 2)
    time.sleep(1.5)
