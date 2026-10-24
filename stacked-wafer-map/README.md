# Stacked Wafer Map

The fails of a 25-wafer lot stacked die by die as each wafer finishes sort: random fails stay faint, while the edge ring and a scratch that repeats on several wafers build up.

See it live at [tofupilot.com/panels#stacked-wafer-map](https://tofupilot.com/panels#stacked-wafer-map).

## How It Works

The value only exists in software, so this is a software view, not an instrument. Each wafer's fails are one path of square-capped points at 24 % opacity, so overlapping wafers add up the way a stacked map counts them. One group bound to `ui.w`, the last wafer sorted, reveals the layers in order (`--k` against `--value`).

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/stacked_wafer_map.py` | The test |
| `plugs/lot_tester.py` | The instrument, mocked |
| `panels/map.html` | The panel |

## Run It

```bash
tofupilot run stacked-wafer-map
```

Replace the mock in `plugs/lot_tester.py` with your wafer sort tester's driver to use it on a real bench.
