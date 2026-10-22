"""Switches the unit on from the 28 V bus supply. The panel's tape follows
`ui.bus` against the 22-36 V input range and turns red outside it with
`ui.bus_state`; `ui.amps` shows the current, inrush included. The run
records the lowest bus voltage under load and the steady-state current."""
import time

INPUT_RANGE_V = (22.0, 36.0)


def power_on(ui, measurements, supply):
    low, last_amps = 99.0, 0.0
    for k in range(supply.length()):
        volts, amps = supply.read()
        ui.bus = volts
        ui.amps = amps
        powered = volts > 1
        ui.bus_state = "alarm" if powered and k > 15 and not INPUT_RANGE_V[0] <= volts <= INPUT_RANGE_V[1] else "ok"
        if amps > 0.1:
            low = min(low, volts)
            last_amps = amps
        time.sleep(0.1)
    measurements.bus_voltage = round(low, 2)
    measurements.steady_current = round(last_amps, 2)
    time.sleep(1.5)
