"""Charges an 8-cell LiFePO4 pack from 20 % to full: constant current,
then constant voltage while the balancer pulls the cells together. The
panel shows the state of charge, the current and every cell live as
display-only `ui` values; the run records three measurements at the end."""
import random
import time

CELLS = 8


def charge(ui, measurements):
    rng = random.Random(7)
    soc, temp = 20.0, 24.0
    offsets = [rng.uniform(-0.04, 0.04) for _ in range(CELLS)]
    for step in range(160):
        current = 10.0 if soc < 85 else max(0.4, 10.0 * (100 - soc) / 15)
        soc = min(100.0, soc + current * 0.055)
        temp += 0.09 * current / 10 - 0.02 * (temp - 24) / 10
        balance = 1 - min(1.0, step / 140)
        cells = [2.9 + 0.0075 * soc + offsets[i] * balance + rng.uniform(-0.002, 0.002) for i in range(CELLS)]
        for i, v in enumerate(cells, start=1):
            setattr(ui, f"cell_{i}", round(v, 3))
        ui.soc = round(soc)
        ui.current = round(current, 1)
        ui.voltage = round(sum(cells), 2)
        ui.temp = round(temp, 1)
        ui.mode = "CC" if soc < 85 else ("CV" if soc < 100 else "FULL")
        time.sleep(0.1)
    measurements.pack_voltage = round(sum(cells), 2)
    measurements.cell_delta = round((max(cells) - min(cells)) * 1000, 1)
    measurements.max_temp = round(temp, 1)
    time.sleep(2)
