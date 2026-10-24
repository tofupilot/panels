"""Folds the data line into an eye and checks it against the USB 2.0
Template 1 mask. `ui.e*_*` are 8 traces of 40 points in mV; each update
replaces the oldest trace and `ui.a*` ages the others so they fade. The run
records the eye height at the centre and the samples inside the mask."""
import time

TRACES, POINTS = 8, 40
MASK = [(0.075, 0), (0.375, 300), (0.625, 300), (0.925, 0)]


def in_mask(t, mv):
    if not 0.075 < t < 0.925:
        return False
    edge = 300 * min(1, (t - 0.075) / 0.3, (0.925 - t) / 0.3)
    return abs(mv) < edge


def eye_mask(ui, measurements, sampling_scope):
    lows, highs, hits = [], [], 0
    for n in range(100):
        slot = n % TRACES
        trace = sampling_scope.trace()
        for k, mv in enumerate(trace):
            setattr(ui, f"e{slot}_{k}", round(mv, 1))
            t = -0.5 + 2 * k / (POINTS - 1)
            hits += in_mask(t, mv)
            if abs(t - 0.5) < 0.06:
                (highs if mv > 0 else lows).append(mv)
        for age in range(TRACES):
            setattr(ui, f"a{(slot - age) % TRACES}", age)
        time.sleep(0.1)
    measurements.eye_height = round(min(highs) - max(lows), 1)
    measurements.mask_hits = hits
    time.sleep(1.5)
