"""Runs twelve boards in parallel on the fixture. `ui.s0` to `ui.s11` are
each slot's state (wait, run, retest, pass) and `ui.p0` to `ui.p11` its
progress. The run records the first-pass yield and the boards passed."""
import time


def parallel_test(ui, measurements, fixture_controller):
    retested = set()
    states = []
    for n in range(160):
        states = fixture_controller.state(n * 0.1)
        for s, (state, progress) in enumerate(states):
            setattr(ui, f"s{s}", state)
            setattr(ui, f"p{s}", round(progress, 3))
            if state == "retest":
                retested.add(s)
        time.sleep(0.1)
    passed = sum(state == "pass" for state, _ in states)
    measurements.first_pass_yield = round(100 * (len(states) - len(retested)) / len(states), 1)
    measurements.boards_passed = passed
    time.sleep(1.5)
