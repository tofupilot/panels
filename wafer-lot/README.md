# Wafer Lot

The 25 wafers of a lot as thumbnails, each one filling in with its fail map when its sort ends, the wafer on the prober outlined; scratched wafers stand out at a glance.

See it live at [tofupilot.com/panels#wafer-lot](https://tofupilot.com/panels#wafer-lot).

## How It Works

The value only exists in software, so this is a software view, not an instrument. Each thumbnail's result (a green disc and its fails as square-capped points) carries its slot as `--k`; one group bound to `ui.w`, the last wafer sorted, reveals them in order. The ring around the wafer on the prober shows only where `--k` is one more than `--value`.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/wafer_lot.py` | The test |
| `plugs/lot_tester.py` | The instrument, mocked |
| `panels/lot.html` | The panel |

## Run It

```bash
tofupilot run wafer-lot
```

Replace the mock in `plugs/lot_tester.py` with your wafer sort tester's driver to use it on a real bench.
