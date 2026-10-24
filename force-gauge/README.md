# Force Gauge

A digital force gauge on a test stand pushing a connector into its header: live force and the held peak on the LCD, and the force against travel with the insertion window.

See it live at [tofupilot.com/panels#force-gauge](https://tofupilot.com/panels#force-gauge).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. The live force is four 7-segment glyphs, `ui.f0` to `ui.f3`, and `ui.peak` the held peak. The curve is 64 points, `ui.c0` to `ui.c63` in newtons at fixed positions of travel, each hidden until it has a value; the peak marker is a group inside a group moved by `ui.pkx` (mm) and `ui.pky` (N).

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/force_gauge.py` | The test |
| `plugs/force_gauge.py` | The instrument, mocked |
| `panels/gauge.html` | The panel |

## Run It

```bash
tofupilot run force-gauge
```

Replace the mock in `plugs/force_gauge.py` with your force gauge's driver to use it on a real bench.
