"""Mock charger and balancer on an 8-cell LiFePO4 pack: constant current to
85 %, then constant voltage while the balancer pulls the cells together.
Replace it with your charger and BMS drivers on a real bench."""
import random

CELLS = 8


class Charger:
    def __init__(self):
        self.rng = random.Random(7)
        self.soc, self.temp, self.step_index = 20.0, 24.0, 0
        self.offsets = [self.rng.uniform(-0.04, 0.04) for _ in range(CELLS)]

    def step(self):
        """Advance the charge by one sample and return the pack's state."""
        current = 10.0 if self.soc < 85 else max(0.4, 10.0 * (100 - self.soc) / 15)
        self.soc = min(100.0, self.soc + current * 0.055)
        self.temp += 0.09 * current / 10 - 0.02 * (self.temp - 24) / 10
        balance = 1 - min(1.0, self.step_index / 140)
        self.step_index += 1
        cells = [
            round(2.9 + 0.0075 * self.soc + self.offsets[i] * balance + self.rng.uniform(-0.002, 0.002), 3)
            for i in range(CELLS)
        ]
        return {
            "soc": round(self.soc),
            "current": round(current, 1),
            "temp": round(self.temp, 1),
            "cells": cells,
            "mode": "CC" if self.soc < 85 else ("CV" if self.soc < 100 else "FULL"),
        }
