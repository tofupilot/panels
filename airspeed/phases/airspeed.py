"""Sweeps the indicated airspeed like a short flight. The needle follows
`ui.ias`, a value only the panel shows, and turns red past the 163 kt red
line. The panel's Zero pitot button (`ui.pressed("tare")`) removes the
probe's offset. The run records the cruise airspeed."""
import time


def sweep(ui, measurements, pitot):
    ui.overspeed = False
    ias = 0.0
    for _ in range(pitot.length()):
        if ui.pressed("tare"):
            pitot.zero()
        label, ias, offset = pitot.read()
        ui.ias = ias
        ui.overspeed = ias > 163
        ui.status = f"{label} · pitot offset {offset:+.0f} kt"
        time.sleep(0.1)
    measurements.cruise_ias = ias
    ui.status = f"Cruise · {ias:.0f} kt"
    time.sleep(2)
