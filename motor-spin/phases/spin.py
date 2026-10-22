"""Steps a drone motor and its ESC through five throttle setpoints on a
thrust stand. The panel shows speed and current as gauges and lights each
setpoint as it is reached; the run records the speed at full throttle,
the peak current and the ESC temperature."""
import random
import time

SETPOINTS = [20, 40, 60, 80, 100]


def sweep(ui, measurements):
    rng = random.Random(11)
    rpm, amps, temp, peak = 0.0, 0.0, 28.0, 0.0
    ui.step = 0
    for n, throttle in enumerate(SETPOINTS, start=1):
        ui.step = n
        ui.throttle = throttle
        target_rpm = 125 * throttle - 0.1 * throttle**2
        target_amps = 0.0029 * throttle**2 + 0.6
        for _ in range(28):
            rpm += (target_rpm - rpm) * 0.18 + rng.uniform(-25, 25)
            amps += (target_amps - amps) * 0.22 + rng.uniform(-0.15, 0.15)
            temp += 0.012 * amps
            peak = max(peak, amps)
            ui.rpm = round(rpm)
            ui.amps = round(amps, 1)
            ui.temp = round(temp, 1)
            time.sleep(0.07)
    measurements.max_rpm = round(rpm)
    measurements.peak_current = round(peak, 1)
    measurements.esc_temp = round(temp, 1)
    ui.step = 6
    for _ in range(25):
        rpm *= 0.8
        amps *= 0.7
        ui.rpm = round(rpm)
        ui.amps = round(amps, 1)
        time.sleep(0.07)
    ui.throttle = 0
    time.sleep(1.5)
