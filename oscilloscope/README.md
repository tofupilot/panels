# Oscilloscope

A 4-channel oscilloscope's screen on a board's power-up: VBUS, the 3.3 V regulator, the MCU leaving reset, then an LED when the firmware boots, captured on a single trigger.

See it live at [tofupilot.com/panels#oscilloscope](https://tofupilot.com/panels#oscilloscope).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. Each trace is 75 points, `ui.c1_0` to `ui.c4_74` in volts, each placed with `translate(var(--x), calc(...))` on the 1 V/div screen and hidden until it has a value, so a capture draws from left to right. `ui.st` is the trigger state, `ui.meas` the measurement row.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/oscilloscope.py` | The test |
| `plugs/oscilloscope.py` | The instrument, mocked |
| `panels/oscilloscope.html` | The panel |

## Run It

```bash
tofupilot run oscilloscope
```

Replace the mock in `plugs/oscilloscope.py` with your oscilloscope's driver to use it on a real bench.
