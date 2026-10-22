"""Charges and discharges the pack on a cycler. The panel's tape follows
`ui.voltage` against the 54.6 V CV setpoint, and turns red under 39.0 V or
over 55.25 V (3.0 and 4.25 V per cell) with `ui.voltage_state`. The run
records the voltage held in CV and the lowest voltage of the discharge."""
import time

UNDERVOLTAGE_V, OVERVOLTAGE_V = 39.0, 55.25


def charge_and_discharge(ui, measurements, cycler):
    cv, low = [], 99.0
    for _ in range(cycler.length()):
        r = cycler.read()
        volts = r["voltage"]
        ui.voltage = round(volts, 2)
        ui.step = r["step"]
        ui.voltage_state = "alarm" if volts < UNDERVOLTAGE_V or volts > OVERVOLTAGE_V else "ok"
        if r["step"] == "CV":
            cv.append(volts)
        if r["step"] == "DSG":
            low = min(low, volts)
        time.sleep(0.1)
    measurements.cv_voltage = round(sum(cv) / len(cv), 2)
    measurements.end_of_discharge_voltage = round(low, 2)
    time.sleep(1.5)
