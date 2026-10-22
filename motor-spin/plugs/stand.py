"""Mock thrust stand with a drone motor and its ESC: follows the throttle
setpoint with the motor's inertia. Replace it with your stand's ESC
controller and load cell drivers on a real bench."""
import random


class ThrustStand:
    def __init__(self):
        self.rng = random.Random(11)
        self.throttle, self.rpm, self.amps, self.temp = 0, 0.0, 0.0, 28.0

    def set_throttle(self, percent):
        self.throttle = percent

    def read(self):
        """[speed in rpm, current in A, ESC temperature in °C] one sample later."""
        t = self.throttle
        target_rpm = 125 * t - 0.1 * t**2
        target_amps = 0.0029 * t**2 + 0.6 if t else 0.0
        if t:
            self.rpm += (target_rpm - self.rpm) * 0.18 + self.rng.uniform(-25, 25)
            self.amps += (target_amps - self.amps) * 0.22 + self.rng.uniform(-0.15, 0.15)
        else:
            self.rpm *= 0.8
            self.amps *= 0.7
        self.temp += 0.012 * self.amps
        return [round(self.rpm), round(self.amps, 1), round(self.temp, 1)]
