"""Reads the AC internal resistance meter clipped to the pack through a
cycle. `ui.r*` and `ui.v*` drive its LCD digits and `ui.comp` its comparator
lamps against the 8.0-12.0 mΩ window. The run records the resistance at rest."""
import time


def show(ui, prefix, text):
    """One 7-segment glyph per character, decimal points left to the panel."""
    for k, ch in enumerate(c for c in text if c != "."):
        setattr(ui, f"{prefix}{k}", "_" if ch == " " else ch)

WINDOW_MOHM = (8.0, 12.0)


def measure(ui, measurements, meter):
    rest = []
    for _ in range(meter.length()):
        mohm, volts, step = meter.read()
        show(ui, "r", f"{mohm:5.3f}")
        show(ui, "v", f"{volts:7.4f}")
        ui.comp = "HI" if mohm > WINDOW_MOHM[1] else "LO" if mohm < WINDOW_MOHM[0] else "IN"
        if step == "REST":
            rest.append(mohm)
        time.sleep(0.1)
    measurements.acir = round(sum(rest) / len(rest), 3)
    time.sleep(1.5)
