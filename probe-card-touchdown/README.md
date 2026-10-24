# Probe Card Touchdown

A 2 x 2 multi-site cantilever probe card seen through its window during wafer sort: each site under the needles takes the bin color of its die at every touchdown, with the touchdown's test time.

See it live at [tofupilot.com/panels#probe-card-touchdown](https://tofupilot.com/panels#probe-card-touchdown).

## How It Works

The value only exists in software, so this is a software view, not an instrument. Each site is a group bound to `ui.s0` to `ui.s3`, the bin of the die under it; CSS picks its color with `[data-value="3"]` and so on, 0 meaning no die under that site at the wafer's edge. `ui.ms` is the touchdown's test time.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/probe_card_touchdown.py` | The test |
| `plugs/probe_card.py` | The instrument, mocked |
| `panels/touchdown.html` | The panel |

## Run It

```bash
tofupilot run probe-card-touchdown
```

Replace the mock in `plugs/probe_card.py` with your probe card and tester's driver to use it on a real bench.
