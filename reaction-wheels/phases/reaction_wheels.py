"""Watches the four reaction wheels in spacecraft telemetry during an
attitude control test. `ui.rw1` to `ui.rw4` are the speeds in rpm on
center-zero bars, `ui.rw1s` to `ui.rw4s` their state (amber past 5000 rpm,
red past 5500 rpm), `ui.h` the total angular momentum. The run records the
highest wheel speed."""
import math
import time

WARN_RPM, SATURATION_RPM, INERTIA = 5000, 5500, 0.0016  # kg·m² per wheel


def watch_wheels(ui, measurements, telemetry):
    peak = 0.0
    for _ in range(telemetry.length()):
        speeds = telemetry.read()
        for k, rpm in enumerate(speeds, start=1):
            setattr(ui, f"rw{k}", round(rpm))
            setattr(ui, f"rw{k}s", "alarm" if abs(rpm) > SATURATION_RPM else "warn" if abs(rpm) > WARN_RPM else "ok")
            peak = max(peak, abs(rpm))
        h = sum(rpm * 2 * math.pi / 60 * INERTIA for rpm in speeds)
        ui.h = f"ΣH {h:.2f} Nms"
        time.sleep(0.1)
    measurements.max_wheel_speed = round(peak)
    time.sleep(1.5)
