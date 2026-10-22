"""Climbs the unit to the selected altitude on a pitot-static tester. The
panel's arc follows `ui.alt`, a value only the panel shows, and its bug
sits on `ui.alt_sel`. The run records the altitude after the level-off."""
import time

SELECTED_FT = 6500


def climb(ui, measurements, tester):
    ui.alt_sel = SELECTED_FT
    alt = 0
    for _ in range(tester.length()):
        alt = tester.read()
        ui.alt = alt
        time.sleep(0.1)
    measurements.level_off_alt = alt
    time.sleep(1.5)
