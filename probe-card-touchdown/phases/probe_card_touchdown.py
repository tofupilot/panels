"""Steps the 2 x 2 probe card across the wafer. At every touchdown `ui.s0` to
`ui.s3` show the bin of the die under each site (0 when the site is off the
wafer) and `ui.ms` the touchdown's test time. The run records the mean test
time and the yield spread between the four sites."""
import time


def touchdowns(ui, measurements, probe_card):
    times, tested, good = [], [0] * 4, [0] * 4
    for _ in range(probe_card.touchdowns()):
        bins, ms = probe_card.touchdown()
        for s, b in enumerate(bins):
            setattr(ui, f"s{s}", b)
            if b:
                tested[s] += 1
                good[s] += b == 1
        ui.ms = f"{ms:.0f} ms"
        times.append(ms)
        time.sleep(0.1)
    yields = [100 * g / t for g, t in zip(good, tested)]
    measurements.touchdown_time = round(sum(times) / len(times), 1)
    measurements.site_yield_spread = round(max(yields) - min(yields), 2)
    time.sleep(1.5)
