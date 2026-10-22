# Airspeed Indicator

An aircraft airspeed indicator: an arc sweeps over the speed bands with the live reading and turns red past the red line.

See it live at [tofupilot.com/panels#airspeed](https://tofupilot.com/panels#airspeed).

## How It Works

`ui.ias`, a value only the panel shows, drives the sweep: an SVG arc with `pathLength="100"` whose `stroke-dasharray` grows with `--value`, and a dot at its tip rotated by the same value. `ui.overspeed`, bound on the panel's root, turns the arc, the tip and the reading red with `[data-value=true]`.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/airspeed.py` | The test |
| `plugs/pitot.py` | The instrument, mocked |
| `panels/airspeed.html` | The panel |

## Run It

```bash
tofupilot run airspeed
```

Replace the mock in `plugs/pitot.py` with your instrument's driver to use it on a real bench.
