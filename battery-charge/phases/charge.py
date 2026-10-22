"""Charges the pack from 20 % to full. The panel shows the state of charge,
the current and every cell live as display-only `ui` values; the run
records three measurements at the end."""
import time


def charge(ui, measurements, charger):
    for _ in range(160):
        state = charger.step()
        for i, volts in enumerate(state["cells"], start=1):
            setattr(ui, f"cell_{i}", volts)
        ui.soc = state["soc"]
        ui.current = state["current"]
        ui.voltage = round(sum(state["cells"]), 2)
        ui.temp = state["temp"]
        ui.mode = state["mode"]
        time.sleep(0.1)
    cells = state["cells"]
    measurements.pack_voltage = round(sum(cells), 2)
    measurements.cell_delta = round((max(cells) - min(cells)) * 1000, 1)
    measurements.max_temp = state["temp"]
    time.sleep(2)
