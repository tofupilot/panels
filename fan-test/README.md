# Cooling Fan Test

Fan blades and airflow lines on looping CSS animations that start and stop with the run, next to live speed and airflow readings.

See it live at [tofupilot.com/panels#fan-test](https://tofupilot.com/panels#fan-test).

## How It Works

The blades and the airflow lines loop on fixed `@keyframes`, declared `paused`. The phase sets `ui.running = True`, and the panel's root, bound with `data-bind="ui.running"`, switches them to `animation-play-state: running` with `[data-value=true]`. The phase never drives the motion: it only sends the readings and records the measurements.

Keyframe names are shared with the page, so they carry the example's name: `fan-test-spin`, `fan-test-flow`, `fan-test-blink`. Readers who prefer reduced motion see the panel still.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/fan.py` | The test, with the fan and the airflow bench mocked |
| `panels/fan.html` | The panel |

## Run It

```bash
tofupilot run fan-test
```

Replace the mock in `phases/fan.py` with your fan controller and anemometer to use it on a real bench.
