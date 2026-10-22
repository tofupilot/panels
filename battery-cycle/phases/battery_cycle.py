"""Charges and discharges the pack and plots the run. Each of `ui.vh0` to
`ui.vh59` and `ui.ih0` to `ui.ih59` is one point of the voltage and current
traces, sent once when the run reaches it. The run records the lowest voltage
of the discharge."""
import time

POINTS = 60


def charge_and_discharge(ui, measurements, cycler):
    total, low = cycler.length(), 99.0
    for n in range(total):
        s = cycler.read()
        volts, amps = s["voltage"], s["current"]
        ui.v = round(volts, 2)
        ui.i = round(amps, 1)
        point = n * POINTS // total
        if point != (n - 1) * POINTS // total or n == 0:
            setattr(ui, f"vh{point}", round(volts, 2))
            setattr(ui, f"ih{point}", round(amps, 1))
        if s["step"] == "DSG":
            low = min(low, volts)
        time.sleep(0.1)
    measurements.end_of_discharge_voltage = round(low, 2)
    time.sleep(1.5)
