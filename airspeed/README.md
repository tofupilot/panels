# Airspeed Indicator

An aircraft airspeed indicator with colored arcs and a red line. The needle follows a live reading and turns red on overspeed.

See it live at [tofupilot.com/panels#airspeed](https://tofupilot.com/panels#airspeed).

## How It Works

`ui.ias`, a value only the panel shows, drives the needle through `--value`. `ui.overspeed` flips the needle red with `:has()`. **Zero pitot** is a `<button name="tare">` the phase reads with `ui.pressed("tare")`.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/airspeed.py` | The test, with the instrument mocked |
| `panels/airspeed.html` | The panel |

## Run It

```bash
tofupilot run airspeed
```

Replace the mock in `phases/airspeed.py` with your instrument's driver to use it on a real bench.
