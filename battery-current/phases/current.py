"""Charges and discharges the pack on a cycler. The panel's center-zero tape
follows `ui.current`, charge positive, and turns red past the -85 A
discharge and +60 A charge limits with `ui.current_state`. The run records
the mean current of the constant-current charge."""
import time

DISCHARGE_LIMIT_A, CHARGE_LIMIT_A = -85, 60


def charge_and_discharge(ui, measurements, cycler):
    cc = []
    for _ in range(cycler.length()):
        r = cycler.read()
        amps = r["current"]
        ui.current = round(amps, 1)
        ui.direction = "CHG" if amps > 0.05 else "DSG" if amps < -0.05 else "—"
        ui.current_state = "alarm" if amps < DISCHARGE_LIMIT_A or amps > CHARGE_LIMIT_A else "ok"
        if r["step"] == "CC":
            cc.append(amps)
        time.sleep(0.1)
    measurements.cc_charge_current = round(sum(cc) / len(cc), 2)
    time.sleep(1.5)
