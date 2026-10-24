# Wafer Map

A 200 mm wafer being probed: the 2 x 2 probe card steps row pair by row pair in a serpentine, and each die takes its bin color as it is tested, edge fails and a scratch included.

See it live at [tofupilot.com/panels#wafer-map](https://tofupilot.com/panels#wafer-map).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The untested wafer is grey rows of dies, each row a single dashed line. Every touchdown's dies are drawn in their bin colors with the touchdown's rank as `--k`; `ui.td`, the touchdown count, shows them once the probe has tested them (`--k` against `--value`), and `ui.tx` and `ui.ty` move the touchdown frame, a group inside a group.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/wafer_map.py` | The test |
| `plugs/prober.py` | The instrument, mocked |
| `panels/map.html` | The panel |

## Run It

```bash
tofupilot run wafer-map
```

Replace the mock in `plugs/prober.py` with your wafer prober's driver to use it on a real bench.
