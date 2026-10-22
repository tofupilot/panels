"""Sweeps the indicated airspeed like a short flight. The needle follows
`ui.ias`, a value only the panel shows; the needle turns red past the
163 kt red line, and the run records the cruise airspeed. The panel's Zero pitot
button (`ui.pressed("tare")`) removes the probe's offset."""
import math
import time


def sweep(ui, measurements):
    profile = [
        ("Takeoff roll", 0, 65, 4.0),
        ("Rotate and climb", 65, 95, 3.0),
        ("Level off, accelerate", 95, 140, 3.0),
        ("Descent: overspeed!", 140, 172, 2.5),
        ("Power back, cruise", 172, 118, 3.0),
    ]
    offset, peak = 6.0, 0.0
    ui.overspeed = False
    for label, v0, v1, seconds in profile:
        ui.status = f"{label} · pitot offset {offset:+.0f} kt"
        steps = int(seconds * 10)
        for i in range(steps + 1):
            if ui.pressed("tare"):
                offset = 0.0
                ui.status = f"{label} · pitot zeroed"
            t = i / steps
            eased = 0.5 - 0.5 * math.cos(math.pi * t)
            ias = v0 + (v1 - v0) * eased + offset + 0.6 * math.sin(i * 1.7)
            peak = max(peak, ias)
            ui.ias = round(ias, 1)
            ui.overspeed = ias > 163
            time.sleep(0.1)
    measurements.cruise_ias = round(ias, 1)
    ui.status = f"Cruise · max {peak:.0f} kt"
    time.sleep(2)
