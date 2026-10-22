# Motor Spin Test

Speed and current arc gauges for a drone motor and ESC, with each throttle setpoint lit as the sweep reaches it.

See it live at [tofupilot.com/panels#motor-spin](https://tofupilot.com/panels#motor-spin).

## How It Works

The arc gauges are SVG paths with `pathLength="100"` and a `stroke-dasharray` computed from `--value`. Each setpoint lights with `opacity: clamp(.18, var(--value) - var(--n) + 1, 1)`, with no JavaScript.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/spin.py` | The test |
| `plugs/stand.py` | The instrument, mocked |
| `panels/spin.html` | The panel |

## Run It

```bash
tofupilot run motor-spin
```

Replace the mock in `plugs/stand.py` with your instrument's driver to use it on a real bench.
