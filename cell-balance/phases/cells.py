"""Charges and discharges the pack on a cycler while the BMS reads the 13
cell voltages. The panel draws each cell's deviation from the mean,
`ui.d1` to `ui.d13` in mV, lights `ui.b1` to `ui.b13` while a cell is
balanced, and turns amber past a 50 mV spread and red past 100 mV with
`ui.cell_state`. The run records the largest spread."""
import time


def charge_and_discharge(ui, measurements, cycler):
    peak = 0.0
    for _ in range(cycler.length()):
        r = cycler.read()
        cells = r["cells"]
        mean = sum(cells) / len(cells)
        for k, (volts, bleeding) in enumerate(zip(cells, r["balancing"]), start=1):
            setattr(ui, f"d{k}", round((volts - mean) * 1000, 1))
            setattr(ui, f"b{k}", bleeding)
        delta = (max(cells) - min(cells)) * 1000
        ui.delta = round(delta)
        ui.mean = round(mean, 3)
        ui.cell_state = "alarm" if delta > 100 else "warn" if delta > 50 else "ok"
        peak = max(peak, delta)
        time.sleep(0.1)
    measurements.max_cell_delta = round(peak)
    time.sleep(1.5)
