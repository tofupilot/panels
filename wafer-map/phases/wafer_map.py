"""Probes one wafer with a 2 x 2 multi-site probe card. Each touchdown reveals
the bins of the dies it tested (`ui.td`, a count) and moves the touchdown frame
(`ui.tx`, `ui.ty`, in mm on the wafer). The run records the wafer yield and
the number of good dies."""
import time

DIE_MM, RADIUS_MM = 7, 100


def sort_wafer(ui, measurements, prober):
    tested = good = 0
    for k in range(prober.touchdowns()):
        row, col, bins = prober.touchdown()
        ui.tx = col * DIE_MM - RADIUS_MM
        ui.ty = row * DIE_MM - RADIUS_MM
        ui.td = k
        tested += sum(b > 0 for b in bins)
        good += sum(b == 1 for b in bins)
        time.sleep(0.1)
    measurements.wafer_yield = round(100 * good / tested, 1)
    measurements.good_dies = good
    time.sleep(1.5)
