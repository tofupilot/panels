"""Charges and discharges the pack. The panel shows `ui.soc` as a reading and
twenty segments, `ui.soc_state` amber under 20 % and red under 10 %, the step
and the charge moved (`ui.ah_in`, `ui.ah_out`). The run records the SOC
reached by the charge."""
import time

HOURS_PER_SAMPLE = 0.3 * 120 / 3600  # 0.3 s of cycle, replayed at 120×


def charge_and_discharge(ui, measurements, cycler):
    peak, ah_in, ah_out = 0.0, 0.0, 0.0
    for _ in range(cycler.length()):
        s = cycler.read()
        soc, amps = s["soc"], s["current"]
        ah_in += max(amps, 0) * HOURS_PER_SAMPLE
        ah_out += max(-amps, 0) * HOURS_PER_SAMPLE
        ui.soc = round(soc, 1)
        ui.soc_state = "alarm" if soc < 10 else "warn" if soc < 20 else "ok"
        ui.step = {"CC": "CC CHARGE", "CV": "CV CHARGE", "DSG": "DISCHARGE"}.get(s["step"], "REST")
        ui.ah_in = round(ah_in, 1)
        ui.ah_out = round(ah_out, 1)
        peak = max(peak, soc)
        time.sleep(0.1)
    measurements.soc_end_of_charge = round(peak, 1)
    time.sleep(1.5)
