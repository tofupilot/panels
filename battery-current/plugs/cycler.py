"""Mock battery cycler: replays a CC-CV charge, a rest and a CC discharge of
a 13S NMC, 50 Ah pack, one reading per call. Replace it with your cycler's and
BMS's drivers on a real bench."""
import math

CELL_OFFSETS = [-0.42, 0.18, 0.05, -0.12, 0.5, -0.3, 0.1, 0.32, -0.05, -0.5, 0.24, 0.0, -0.2]
SENSORS = [("T1 CELL 1", -1.5), ("T2 CELL 4", 0.0), ("T3 CELL 7", 1.2), ("T4 BUSBAR", 4.6),
           ("T5 CELL 10", -0.8), ("T6 CELL 13", 0.4), ("T7 INLET", -2.0), ("T8 OUTLET", 0.9)]
STEPS = [("CC", 0, 18), ("CV", 18, 28), ("REST", 28, 33), ("DSG", 33, 53), ("REST", 53, 60)]
CYCLE_S, DT = 60, 0.3


def _lerp(a, b, x):
    return a + (b - a) * min(1.0, max(0.0, x))


def _ease(x):
    return 0.5 - 0.5 * math.cos(math.pi * min(1.0, max(0.0, x)))


def _wob(t, k):
    return math.sin(t * k) * 0.5 + math.sin(t * k * 2.3) * 0.25


class BatteryCycler:
    def __init__(self):
        self.t = 0.0

    def length(self):
        return int(CYCLE_S / DT)

    def read(self):
        """One reading: step, SOC %, pack V, pack A (charge positive),
        temperatures by sensor in °C, cell voltages in V, cells balancing."""
        t = self.t
        self.t += DT
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
        step = next(name for name, a, b in STEPS if a <= t < b) if t < CYCLE_S else "REST"
        temps = {
            name: temp + offset * (0.4 + (temp - 24) / 30) + _wob(t + k, 1.1) * 0.15
            for k, (name, offset) in enumerate(SENSORS)
        }
        cells = [v / 13 + offset * delta / 1000 for offset in CELL_OFFSETS]
        balancing = [bleed and offset > 0.15 for offset in CELL_OFFSETS]
        return {"step": step, "soc": soc, "voltage": v, "current": i,
                "temperatures": temps, "cells": cells, "balancing": balancing}
