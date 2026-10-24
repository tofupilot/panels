"""Captures the TMP117 temperature read three times. `ui.sweep` reveals the
capture from left to right, `ui.temp` shows the decoded temperature. The run
records the temperature: 0x0C80 at 7.8125 m°C per bit is 25.00 °C."""
import time


def sensor_read(ui, measurements, logic_analyzer):
    celsius = 0.0
    for _ in range(3):
        ui.sweep = 0
        time.sleep(0.4)
        frame = logic_analyzer.capture()
        for k in range(1, 21):
            ui.sweep = round(k / 20, 3)
            time.sleep(0.1)
        raw = (frame["data"][0] << 8) | frame["data"][1]
        if raw & 0x8000:
            raw -= 1 << 16
        celsius = raw * 0.0078125
        ui.temp = f"{celsius:.2f} °C"
        time.sleep(1.6)
    measurements.temperature = round(celsius, 2)
    time.sleep(0.5)
