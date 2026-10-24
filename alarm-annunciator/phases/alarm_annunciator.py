"""Watches the station's alarms through one incident and drives the
annunciator: each window is bound to its alarm, "first" for the first-out
(fast flash), "new" for a later one (slow flash), "on" once acknowledged,
"" when clear. The run records how many alarms are still active at the end."""
import time

ALARMS = ["e_stop", "overtemp", "vac_loss", "hv_on", "low_air", "door_open", "fixture_open", "dut_power"]
DURATION_S = 10.0


def watch(ui, measurements, annunciator):
    t, states = 0.0, {}
    while t < DURATION_S:
        states = annunciator.states(t)
        for name in ALARMS:
            setattr(ui, name, states.get(name, ""))
        t += 0.1
        time.sleep(0.1)
    measurements.alarms_at_end = sum(1 for name, s in states.items() if s and name != "dut_power")
    time.sleep(1.5)
