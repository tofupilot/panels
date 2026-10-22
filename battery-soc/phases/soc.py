"""Charges and discharges the pack on a cycler. The panel shows `ui.soc`
in a battery outline and `ui.step`, and turns amber under 20 % and red under
10 % with `ui.soc_state`. The run records the SOC reached by the charge."""
import time


def charge_and_discharge(ui, measurements, cycler):
    peak = 0.0
    for _ in range(cycler.length()):
        r = cycler.read()
        ui.soc = round(r["soc"], 1)
        ui.step = r["step"]
        ui.soc_state = "alarm" if r["soc"] < 10 else "warn" if r["soc"] < 20 else "ok"
        peak = max(peak, r["soc"])
        time.sleep(0.1)
    measurements.soc_end_of_charge = round(peak, 1)
    time.sleep(1.5)
