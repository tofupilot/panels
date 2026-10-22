"""Charges and discharges the pack on a cycler while eight thermistors are
read. The panel puts `ui.t1` to `ui.t8` on one scale, shows the hottest with
`ui.tmax` and `ui.hot`, and moves its limits with `ui.charging`: 45 °C while
charging, 60 °C while discharging, amber 5 °C before. The run records the
highest temperature."""
import time

LIMITS = {True: (40, 45), False: (55, 60)}


def charge_and_discharge(ui, measurements, cycler):
    peak = 0.0
    for _ in range(cycler.length()):
        r = cycler.read()
        temps = r["temperatures"]
        for k, value in enumerate(temps.values(), start=1):
            setattr(ui, f"t{k}", round(value, 1))
        hot = max(temps, key=temps.get)
        tmax = temps[hot]
        charging = r["current"] > 0.05
        warn, alarm = LIMITS[charging]
        ui.tmax = round(tmax, 1)
        ui.hot = hot
        ui.spread = round(tmax - min(temps.values()), 1)
        ui.charging = charging
        ui.temp_state = "alarm" if tmax > alarm else "warn" if tmax > warn else "ok"
        peak = max(peak, tmax)
        time.sleep(0.1)
    measurements.max_temperature = round(peak, 1)
    time.sleep(1.5)
