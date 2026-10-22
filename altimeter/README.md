# Altimeter

An altimeter: an arc sweeps up to the live altitude while a cyan bug marks the selected one, and the reading stays in the center.

See it live at [tofupilot.com/panels#altimeter](https://tofupilot.com/panels#altimeter).

## How It Works

`ui.alt`, a value only the panel shows, drives the sweep: an SVG arc with `pathLength="100"` whose `stroke-dasharray` grows with `--value`, over 0 to 10,000 ft, and a dot at its tip rotated by the same value. `ui.alt_sel` turns the cyan bug to the selected altitude.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/altimeter.py` | The test |
| `plugs/pitot_static.py` | The instrument, mocked |
| `panels/altimeter.html` | The panel |

## Run It

```bash
tofupilot run altimeter
```

Replace the mock in `plugs/pitot_static.py` with your pitot-static tester's driver to use it on a real bench.
