"""Turns the unit to the selected heading on a turntable. The panel's card
follows `ui.hdg`, a value only the panel shows, and its bug sits on
`ui.hdg_bug`. The run records the heading after the turn."""
import time

SELECTED_DEG = 270


def turn(ui, measurements, turntable):
    ui.hdg_bug = SELECTED_DEG
    heading = 0.0
    for _ in range(turntable.length()):
        heading = turntable.read()
        ui.hdg = heading
        time.sleep(0.1)
    measurements.final_heading = heading
    time.sleep(1.5)
