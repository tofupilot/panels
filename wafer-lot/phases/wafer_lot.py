"""Sorts the lot wafer by wafer: `ui.w`, the last wafer sorted, fills in its
thumbnail and moves the outline to the next one on the prober. The run records
the lot yield and the number of wafers sorted."""
import time


def sort_lot(ui, measurements, lot_tester):
    good = total = 0
    count = lot_tester.wafers()
    for w in range(count):
        bins = lot_tester.sort()
        good += sum(b == 1 for b in bins)
        total += len(bins)
        ui.w = w
        time.sleep(0.6)
    measurements.lot_yield = round(100 * good / total, 2)
    measurements.wafers_sorted = count
    time.sleep(1.5)
