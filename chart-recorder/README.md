# Chart Recorder

A two-pen paper chart recorder on a climatic chamber: temperature in red, humidity in blue, the paper feeding down as the chamber runs a cold soak and a damp-heat dwell.

See it live at [tofupilot.com/panels#chart-recorder](https://tofupilot.com/panels#chart-recorder).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. The ink is a pool of 66 points written round-robin: each update fills one slot, `ui.t7` and `ui.h7` with the readings and `ui.y7` with the row number. The paper, bound to `ui.feed`, slides down one row per update, so older ink scrolls away under the pens; `ui.t` and `ui.h` move the pens.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/chart_recorder.py` | The test |
| `plugs/chart_recorder.py` | The instrument, mocked |
| `panels/recorder.html` | The panel |

## Run It

```bash
tofupilot run chart-recorder
```

Replace the mock in `plugs/chart_recorder.py` with your chart recorder's driver to use it on a real bench.
