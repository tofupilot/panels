# Burn-in Heat Map

A thermal camera's view of a board in burn-in, laid over its KiCad layout: the MCU and the regulator heat up, and the hottest point is marked with its temperature.

See it live at [tofupilot.com/panels#burn-in-heat-map](https://tofupilot.com/panels#burn-in-heat-map).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The board is SVG exported from the KiCad layout. The heat map is 108 cells, `ui.h0` to `ui.h107` in °C, each colored from its own `--value` with `hsl(calc(...))` and fading in above 31 °C. `ui.hx` and `ui.hy` move the hot spot marker, `ui.tmax` is its reading. The board is the GreatFET One by Great Scott Gadgets (BSD-3-Clause), drawn from its KiCad layout (github.com/greatscottgadgets/greatfet-hardware, azalea).

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/burn_in_heat_map.py` | The test |
| `plugs/thermal_camera.py` | The instrument, mocked |
| `panels/map.html` | The panel |

## Run It

```bash
tofupilot run burn-in-heat-map
```

Replace the mock in `plugs/thermal_camera.py` with your thermal camera's driver to use it on a real bench.
