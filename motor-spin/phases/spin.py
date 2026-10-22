"""Steps the motor through five throttle setpoints. The panel shows speed
and current as gauges and lights each setpoint as it is reached; the run
records the speed at full throttle, the peak current and the ESC temperature."""
import time

SETPOINTS = [20, 40, 60, 80, 100]


def sweep(ui, measurements, stand):
    peak = 0.0
    ui.step = 0
    for n, throttle in enumerate(SETPOINTS, start=1):
        ui.step = n
        ui.throttle = throttle
        stand.set_throttle(throttle)
        for _ in range(28):
            rpm, amps, temp = stand.read()
            peak = max(peak, amps)
            ui.rpm, ui.amps, ui.temp = rpm, amps, temp
            time.sleep(0.07)
    measurements.max_rpm = rpm
    measurements.peak_current = round(peak, 1)
    measurements.esc_temp = temp
    ui.step = 6
    stand.set_throttle(0)
    for _ in range(25):
        rpm, amps, _ = stand.read()
        ui.rpm, ui.amps = rpm, amps
        time.sleep(0.07)
    ui.throttle = 0
    time.sleep(1.5)
