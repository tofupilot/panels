# Process Capability

A measurement's histogram filling board by board against its lower and upper limits, with the normal fit drawn over it, the way a quality engineer judges Cpk.

See it live at [tofupilot.com/panels#process-capability](https://tofupilot.com/panels#process-capability).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The histogram is 24 bars of 25 mV, `ui.b0` to `ui.b23`, each a count scaled with `scaleY(...)`. The normal fit is 49 points, `ui.f0` to `ui.f48`, recomputed from the running mean and sigma. The limits are static.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/process_capability.py` | The test |
| `plugs/production_line.py` | The instrument, mocked |
| `panels/capability.html` | The panel |

## Run It

```bash
tofupilot run process-capability
```

Replace the mock in `plugs/production_line.py` with your production line's driver to use it on a real bench.
