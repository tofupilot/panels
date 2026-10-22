# Battery Cycler Channel

The front panel of a battery cycler channel: terminal voltage and current on a fluorescent display, the CC and CV mode, the direction, and the overcurrent trip.

See it live at [tofupilot.com/panels#battery-cycler](https://tofupilot.com/panels#battery-cycler).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. Each digit is a group bound to one character (`ui.v0` to `ui.v3`, `ui.i0` to `ui.i3`) and CSS lights its segments with `[data-value="5"]` and so on. `ui.cc`, `ui.cv`, `ui.chg`, `ui.dsg`, `ui.ocp` and `ui.out` light the annunciators; `ui.ocp`, bound on the panel's root, turns the current red.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/battery_cycler.py` | The test |
| `plugs/cycler.py` | The instrument, mocked |
| `panels/cycler.html` | The panel |

## Run It

```bash
tofupilot run battery-cycler
```

Replace the mock in `plugs/cycler.py` with your battery cycler's driver to use it on a real bench.
