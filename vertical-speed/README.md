# Vertical Speed Indicator

A vertical speed indicator: an arc fills up from zero in a climb and down in a descent, and turns red past the sink rate limit.

See it live at [tofupilot.com/panels#vertical-speed](https://tofupilot.com/panels#vertical-speed).

## How It Works

`ui.vs`, a value only the panel shows, drives two SVG arcs from zero at 9 o'clock: the upper one fills with `clamp(0, var(--value), 2000)`, the lower one with `clamp(0, var(--value) * -1, 2000)`, so only one fills at a time. `ui.sink`, bound on the panel's root, turns the descent red with `[data-value=true]`.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/vertical_speed.py` | The test |
| `plugs/pitot_static.py` | The instrument, mocked |
| `panels/vsi.html` | The panel |

## Run It

```bash
tofupilot run vertical-speed
```

Replace the mock in `plugs/pitot_static.py` with your pitot-static tester's driver to use it on a real bench.
