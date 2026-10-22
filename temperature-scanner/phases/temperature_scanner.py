"""Scans eight thermocouples on the pack while it charges and discharges.
`ui.t1_*` to `ui.t8_*` drive each channel's digits; `ui.a1` to `ui.a8` show HI
or ALM against the step's limit: 45 °C charging, 60 °C discharging, HI 5 °C
before. The run records the highest temperature."""
import time


def show(ui, prefix, text):
    """One 7-segment glyph per character, decimal points left to the panel."""
    for k, ch in enumerate(c for c in text if c != "."):
        setattr(ui, f"{prefix}{k}", "_" if ch == " " else ch)

LIMITS = {True: (40, 45), False: (55, 60)}


def scan(ui, measurements, scanner):
    peak = 0.0
    for _ in range(scanner.length()):
        temps, charging = scanner.read()
        warn, alarm = LIMITS[charging]
        for k, c in enumerate(temps, start=1):
            show(ui, f"t{k}_", f"{c:4.1f}")
            setattr(ui, f"a{k}", "ALM" if c > alarm else "HI" if c > warn else "")
        ui.mode = f"LIMIT {alarm} °C · {'CHARGE' if charging else 'DISCHARGE'}"
        peak = max(peak, *temps)
        time.sleep(0.1)
    measurements.max_temperature = round(peak, 1)
    time.sleep(1.5)
