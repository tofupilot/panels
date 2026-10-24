"""Logs the climatic chamber on the two-pen chart recorder. Each update writes
one row into a pool of 66 ink slots round-robin (`ui.t*`, `ui.h*` with the
readings, `ui.y*` with the row number) and moves the paper on with `ui.feed`;
`ui.t` and `ui.h` drive the pens. The run records the damp-heat dwell."""
import time

SLOTS = 66


def record(ui, measurements, chart_recorder):
    dwell_t, dwell_h = [], []
    for row in range(chart_recorder.length()):
        temp, rh, in_dwell = chart_recorder.read()
        slot = row % SLOTS
        setattr(ui, f"y{slot}", row)
        setattr(ui, f"t{slot}", round(temp, 2))
        setattr(ui, f"h{slot}", round(rh, 2))
        ui.feed = row
        ui.t, ui.h = round(temp, 2), round(rh, 2)
        if in_dwell:
            dwell_t.append(temp)
            dwell_h.append(rh)
        time.sleep(0.1)
    measurements.dwell_temperature = round(sum(dwell_t) / len(dwell_t), 2)
    measurements.dwell_humidity = round(sum(dwell_h) / len(dwell_h), 2)
    time.sleep(1.5)
