"""Pitches and banks the unit on a tilt table. The panel's horizon follows
`ui.pitch` and `ui.roll`, values only the panel shows. The run records the
attitude the unit reads once it is level again."""
import time


def maneuver(ui, measurements, table):
    pitch = roll = 0.0
    for _ in range(table.length()):
        pitch, roll = table.read()
        ui.pitch = pitch
        ui.roll = roll
        time.sleep(0.1)
    measurements.level_pitch = pitch
    measurements.level_roll = roll
    time.sleep(1.5)
