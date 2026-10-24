"""Pushes the connector in on the test stand and reads the force gauge. `ui.f*`
drive the LCD's live force, `ui.peak` the held peak, `ui.c0` to `ui.c63` the
force-travel curve and `ui.pkx` / `ui.pky` the peak marker. The run records
the insertion peak and where it occurred."""
import time


def show(ui, prefix, text):
    """One 7-segment glyph per character, decimal points left to the panel."""
    for k, ch in enumerate(c for c in text if c != "."):
        setattr(ui, f"{prefix}{k}", "_" if ch == " " else ch)

POINTS, TRAVEL_MM, WINDOW_MM = 64, 5.6, (1.5, 4.5)


def insert(ui, measurements, force_gauge):
    peak, at = 0.0, 0.0
    for _ in range(3):
        for k in range(POINTS):
            mm = k / (POINTS - 1) * TRAVEL_MM
            newtons = force_gauge.read(mm)
            setattr(ui, f"c{k}", round(newtons, 2))
            show(ui, "f", f"{max(0.0, min(newtons, 99.99)):5.2f}")
            if WINDOW_MM[0] <= mm <= WINDOW_MM[1] and newtons > peak:
                peak, at = newtons, mm
                ui.peak = f"{peak:.2f}"
                ui.pkx, ui.pky = round(at, 2), round(peak, 2)
            time.sleep(0.1)
        time.sleep(0.8)
        if _ < 2:
            peak = 0.0
    measurements.insertion_peak = round(peak, 2)
    measurements.peak_travel = round(at, 2)
    time.sleep(1.5)
