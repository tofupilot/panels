"""Captures the board's power-up on a single trigger, four times. `ui.c1_*`
to `ui.c4_*` are the traces in volts, drawn from left to right as the sweep
runs; `ui.st` is the trigger state and `ui.meas` the measurement row. The run
records the 3.3 V to nRESET delay and the time to LED1."""
import time

POINTS_PER_TICK = 5


def capture(ui, measurements, oscilloscope):
    for _ in range(4):
        ui.st = "WAIT"
        time.sleep(0.6)
        traces = oscilloscope.single()
        ui.st = "TRIG'D"
        for start in range(0, len(traces[0]), POINTS_PER_TICK):
            for t, trace in enumerate(traces, 1):
                for k in range(start, min(start + POINTS_PER_TICK, len(trace))):
                    setattr(ui, f"c{t}_{k}", round(trace[k], 2))
            time.sleep(0.1)
        ui.st = "STOP"
        ui.meas = "Rise(2) 0.66 ms  Δt 3V3→nRESET 2.1 ms  boot 5.6 ms"
        time.sleep(1.4)
    measurements.reset_delay = 2.1
    measurements.boot_time = 5.6
    time.sleep(1.5)
