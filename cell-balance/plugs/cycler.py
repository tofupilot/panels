"""Mock instrument replaying a simulated 13S NMC, 50 Ah pack through a CC-CV
charge, a rest and a 75 A discharge."""
import math

CELL_OFFSETS = [-0.42, 0.18, 0.05, -0.12, 0.5, -0.3, 0.1, 0.32, -0.05, -0.5, 0.24, 0.0, -0.2]
SENSORS = [("CELL 1", -1.5), ("CELL 4", 0.0), ("CELL 7", 1.2), ("BUSBAR", 4.6),
           ("CELL 10", -0.8), ("CELL 13", 0.4), ("INLET", -2.0), ("OUTLET", 0.9)]
STEPS = [("CC", 0, 18), ("CV", 18, 28), ("REST", 28, 33), ("DSG", 33, 53), ("REST", 53, 60)]
CYCLE_S, DT = 60, 0.3


def _lerp(a, b, x):
    return a + (b - a) * min(1.0, max(0.0, x))


def _ease(x):
    return 0.5 - 0.5 * math.cos(math.pi * min(1.0, max(0.0, x)))


def _wob(t, k):
    return math.sin(t * k) * 0.5 + math.sin(t * k * 2.3) * 0.25


def pack_state(t):
    """The simulated 13S NMC, 50 Ah pack at cycle time t (s): CC 50 A to
    54.6 V, CV to 2.5 A, rest, 75 A discharge with a current spike, rest."""
    bleed = False
    if t < 18:
        x = t / 18
        soc, i = _lerp(20, 78, x), 50 + _wob(t, 3) * 0.4
        v, temp, delta = 46.2 + 8.4 * x ** 1.6, _lerp(24, 31, x), _lerp(8, 14, x)
    elif t < 28:
        x = (t - 18) / 10
        soc, i = _lerp(78, 99, _ease(x)), 2.5 + 47.5 * math.exp(-3.2 * x)
        v, temp = 54.6, _lerp(31, 33, x)
        delta = _lerp(14, 26, _ease(x * 1.4)) - _lerp(0, 8, (x - 0.6) / 0.4)
        bleed = True
    elif t < 33:
        x = (t - 28) / 5
        soc, i, v = 99, 0.0, _lerp(54.6, 54.0, _ease(x))
        temp, delta, bleed = _lerp(33, 30, x), _lerp(18, 10, x), x < 0.6
    elif t < 53:
        x = (t - 33) / 20
        spike = -17 * math.sin(math.pi * (t - 38) / 2.5) if 38 < t < 40.5 else 0.0
        soc, i = _lerp(99, 22, x), -75 + spike + _wob(t, 2.7) * 0.6
        v = 53.4 - 5.2 * x - 1.6 * x ** 6 + spike * 0.03
        temp, delta = _lerp(30, 50, x ** 0.9), _lerp(10, 58, x ** 2.2)
    else:
        x = (t - 53) / 7
        soc, i, v = 22, 0.0, _lerp(46.6, 47.4, _ease(x))
        temp, delta = _lerp(50, 47, x), _lerp(58, 44, x)
    step = next((name for name, a, b in STEPS if a <= t < b), "REST")
    temps = [temp + o * (0.4 + (temp - 24) / 30) + _wob(t + k, 1.1) * 0.15 for k, (_, o) in enumerate(SENSORS)]
    cells = [v / 13 + o * delta / 1000 for o in CELL_OFFSETS]
    balancing = [bleed and o > 0.15 for o in CELL_OFFSETS]
    acir = 9.6 * (1 - 0.006 * (temp - 25)) + 0.02 * math.sin(t * 2.3)
    return {"step": step, "soc": soc, "voltage": v, "current": i, "temperatures": temps,
            "cells": cells, "balancing": balancing, "acir_mohm": acir}


class _Replay:
    def __init__(self):
        self.t = 0.0

    def length(self):
        return int(CYCLE_S / DT)

    def _next(self):
        state = pack_state(self.t)
        self.t += DT
        return state


class BatteryCycler(_Replay):
    """Mock battery cycler channel. Replace it with your cycler's driver."""

    def read(self):
        """The channel and the pack it reads: step, SOC %, V, A (charge
        positive), cell voltages and balancing from the BMS."""
        return self._next()
