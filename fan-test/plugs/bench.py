"""Mock airflow bench with a cooling fan: spins up toward full duty with the
rotor's inertia. Replace it with your fan controller, tachometer and
anemometer drivers on a real bench."""
import random

FULL_RPM = 3020
CFM_AT_FULL = 44.5


class AirflowBench:
    def __init__(self):
        self.rng = random.Random(5)
        self.on, self.rpm = False, 0.0

    def start(self):
        self.on = True

    def stop(self):
        self.on = False

    def read(self):
        """[speed in rpm, airflow in CFM] one sample later."""
        target = FULL_RPM if self.on else 0
        self.rpm += (target - self.rpm) * 0.06 + (self.rng.uniform(-8, 8) if self.on else 0)
        return [round(self.rpm), round(self.rpm / FULL_RPM * CFM_AT_FULL, 1)]

    def noise(self):
        """Sound level at 1 m, in dB(A)."""
        return round(34.8 + self.rng.uniform(-0.4, 0.4), 1)
