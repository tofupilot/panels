# Parametric Wafer Map

Each die's threshold voltage measured during wafer sort, drawn on the wafer as a heat map from 430 to 460 mV: the radial rise toward the edge shows up as the probe card steps across.

See it live at [tofupilot.com/panels#parametric-wafer-map](https://tofupilot.com/panels#parametric-wafer-map).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The untested wafer is grey rows of dies. Every touchdown's dies are drawn in 16 color levels of Vth with the touchdown's rank as `--k`; `ui.td`, the touchdown count, shows them as they are measured. The color scale is drawn once beside the wafer.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/parametric_wafer_map.py` | The test |
| `plugs/parametric_tester.py` | The instrument, mocked |
| `panels/map.html` | The panel |

## Run It

```bash
tofupilot run parametric-wafer-map
```

Replace the mock in `plugs/parametric_tester.py` with your parametric tester's driver to use it on a real bench.
