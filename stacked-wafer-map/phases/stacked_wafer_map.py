"""Sorts the lot wafer by wafer and stacks each wafer's fails on the map
(`ui.w`, the last wafer sorted). The run records how many dies failed on 4 or
more wafers, and the lot yield."""
import time


def stack_lot(ui, measurements, lot_tester):
    fails, good, total = None, 0, 0
    for w in range(lot_tester.wafers()):
        bins = lot_tester.sort()
        fails = [0] * len(bins) if fails is None else fails
        for i, b in enumerate(bins):
            fails[i] += b != 1
        good += sum(b == 1 for b in bins)
        total += len(bins)
        ui.w = w
        time.sleep(0.6)
    measurements.repeating_fail_dies = sum(n >= 4 for n in fails)
    measurements.lot_yield = round(100 * good / total, 2)
    time.sleep(1.5)
