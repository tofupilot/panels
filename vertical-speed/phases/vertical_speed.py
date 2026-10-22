"""Climbs and descends the unit on a pitot-static tester. The panel's arcs
follow `ui.vs`, a value only the panel shows, and turn red past a 1,500 fpm
sink rate with `ui.sink`. The run records the mean vertical speed of the
steady climb."""
import time

SINK_LIMIT_FPM = -1500


def climb_and_descend(ui, measurements, tester):
    ui.sink = False
    climb = []
    for _ in range(tester.length()):
        segment, fpm = tester.read()
        ui.vs = fpm
        ui.sink = fpm < SINK_LIMIT_FPM
        if segment == "climb":
            climb.append(fpm)
        time.sleep(0.1)
    measurements.climb_rate = round(sum(climb) / len(climb))
    time.sleep(1.5)
