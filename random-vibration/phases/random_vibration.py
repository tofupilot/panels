"""Runs random vibration at -12, -6, -3 dB and full level. The panel lights
`ui.level`, fills the tape with `ui.grms`, puts the GEVS ±10 % RMS band
around `ui.reference`, and turns red with `ui.vibe_state` outside it once the
level has settled. The run records the mean control Grms at full level."""
import time

TOLERANCE = 0.10


def random_vibration(ui, measurements, shaker):
    full, settled = [], 0
    for _ in range(shaker.length()):
        level, reference, grms = shaker.read()
        ui.level = "stop" if level is None else str(level)
        ui.reference = round(reference, 2)
        ui.grms = round(grms, 2)
        settled = settled + 1 if level is not None else 0
        out = level is not None and settled > 8 and abs(grms - reference) > TOLERANCE * reference
        ui.vibe_state = "alarm" if out else "ok"
        if level == 0 and settled > 8:
            full.append(grms)
        time.sleep(0.1)
    measurements.full_level_grms = round(sum(full) / len(full), 2)
    time.sleep(1.5)
