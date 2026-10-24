# LED Color

An LED analyzer's reading of a board's eight LEDs on the CIE 1931 chromaticity diagram: each LED's point drops into its bin, the ANSI 5700 K quadrangle for the white one.

See it live at [tofupilot.com/panels#led-color](https://tofupilot.com/panels#led-color).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The spectral locus is drawn from the CIE 1931 2° table and the bins are fixed paths. Each LED is a group bound to `ui.d1` to `ui.d8`: it fades in and drops onto its chromaticity when the phase sends `measured`. The ring is a group inside a group: `ui.cx` and `ui.cy` move it to the LED being read.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/led_color.py` | The test |
| `plugs/led_analyzer.py` | The instrument, mocked |
| `panels/color.html` | The panel |

## Run It

```bash
tofupilot run led-color
```

Replace the mock in `plugs/led_analyzer.py` with your led analyzer's driver to use it on a real bench.
