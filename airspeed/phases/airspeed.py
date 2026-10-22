"""Sweeps the indicated airspeed like a short flight. The panel's arc follows
`ui.ias`, a value only the panel shows, and turns red past the 163 kt red
line with `ui.overspeed`. The run records the cruise airspeed."""
import time


def sweep(ui, measurements, pitot):
    ui.overspeed = False
    ias = 0.0
    for _ in range(pitot.length()):
        ias = pitot.read()
        ui.ias = ias
        ui.overspeed = ias > 163
        time.sleep(0.1)
    measurements.cruise_ias = ias
    time.sleep(2)
