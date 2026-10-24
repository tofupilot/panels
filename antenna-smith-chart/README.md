# Antenna Match on a Smith Chart

A vector network analyzer's S11 sweep of a 2.4 GHz antenna on the Smith chart: the trace curls toward the centre as the matching network is tuned, with the 2.45 GHz marker and the VSWR 2 circle.

See it live at [tofupilot.com/panels#antenna-smith-chart](https://tofupilot.com/panels#antenna-smith-chart).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The sweep is 41 points, each a group inside a group: `ui.sx0` to `ui.sx40` move them across with the reflection coefficient's real part and `ui.sy0` to `ui.sy40` up with its imaginary part, on a chart of radius 1. Point 20 is the 2.45 GHz marker. The grid and the VSWR 2 circle are static.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/antenna_smith_chart.py` | The test |
| `plugs/vna.py` | The instrument, mocked |
| `panels/chart.html` | The panel |

## Run It

```bash
tofupilot run antenna-smith-chart
```

Replace the mock in `plugs/vna.py` with your vector network analyzer's driver to use it on a real bench.
