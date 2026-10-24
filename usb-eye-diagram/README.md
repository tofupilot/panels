# USB 2.0 Eye and Mask

A USB 2.0 high-speed data line folded into an eye on the oscilloscope, traces fading with persistence, against the hexagonal Template 1 mask and the level limits.

See it live at [tofupilot.com/panels#usb-eye-diagram](https://tofupilot.com/panels#usb-eye-diagram).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The eye is a fixed pool of 8 traces of 40 points, `ui.e0_0` to `ui.e7_39` in mV, each placed with `translate(var(--x), calc(...))`. Every update replaces the oldest trace, and `ui.a0` to `ui.a7`, each trace's age, fade it out. The mask and the level limits are static.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/usb_eye_diagram.py` | The test |
| `plugs/sampling_scope.py` | The instrument, mocked |
| `panels/diagram.html` | The panel |

## Run It

```bash
tofupilot run usb-eye-diagram
```

Replace the mock in `plugs/sampling_scope.py` with your sampling oscilloscope's driver to use it on a real bench.
