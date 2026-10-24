"""Runs a pressure-decay leak test and shows it on the Bourdon gauge: `ui.bar`
turns the needle, `ui.peak` the red drag pointer. The run records the test
pressure and the decay rate over the 10 s test."""
import time

TEST_S = 10


def leak_test(ui, measurements, leak_tester):
    peak, held, decay = 0.0, 0.0, 0.0
    for _ in range(leak_tester.length()):
        step, bar, decay_pa = leak_tester.read()
        peak = max(peak, bar)
        ui.bar = round(bar, 3)
        ui.peak = round(peak, 3)
        if step == "test":
            held, decay = bar, decay_pa
        time.sleep(0.1)
    measurements.test_pressure = round(held, 2)
    measurements.decay_rate = round(decay / TEST_S * 60, 1)
    time.sleep(1.5)
