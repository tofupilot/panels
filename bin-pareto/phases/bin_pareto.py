"""Sorts the lot wafer by wafer and counts the fails by bin: `ui.b2` to `ui.b5`
grow the pareto's bars as each wafer's dies come in. The run records the share
of fails in the leading bin and the lot yield."""
import time

FAIL_BINS = (2, 3, 4, 5)


def bin_pareto(ui, measurements, lot_tester):
    counts = dict.fromkeys(FAIL_BINS, 0)
    good = total = 0
    for _ in range(lot_tester.wafers()):
        bins = lot_tester.sort()
        good += sum(b == 1 for b in bins)
        total += len(bins)
        # Six updates per wafer, so the bars grow while the wafer is probed.
        for part in range(1, 7):
            chunk = bins[(part - 1) * len(bins) // 6: part * len(bins) // 6]
            for b in FAIL_BINS:
                counts[b] += chunk.count(b)
                setattr(ui, f"b{b}", counts[b])
            time.sleep(0.1)
    measurements.top_bin_share = round(100 * max(counts.values()) / sum(counts.values()), 1)
    measurements.lot_yield = round(100 * good / total, 2)
    time.sleep(1.5)
