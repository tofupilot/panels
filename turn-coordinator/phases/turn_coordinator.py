"""Turns the unit at standard rate on a rate table. The panel's aircraft
banks with `ui.rate` and its ball follows `ui.slip`, values only the panel
shows. The run records the mean rate and slip of the steady turn."""
import time


def standard_rate_turn(ui, measurements, table):
    rates, slips = [], []
    for _ in range(table.length()):
        rate, slip = table.read()
        ui.rate = rate
        ui.slip = slip
        if table.in_turn():
            rates.append(rate)
            slips.append(slip)
        time.sleep(0.1)
    measurements.turn_rate = round(sum(rates) / len(rates), 2)
    measurements.slip = round(sum(slips) / len(slips), 2)
    time.sleep(1.5)
