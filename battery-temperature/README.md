# Max Temperature

Eight thermistors as dots on one temperature scale, with the hottest one named and limits that follow charge or discharge.

See it live at [tofupilot.com/panels#battery-temperature](https://tofupilot.com/panels#battery-temperature).

## How It Works

Each of `ui.t1` to `ui.t8` places a dot with `left: calc(...)` on one 10-70 °C scale, so the spread and the hot spot read at a glance. `ui.charging`, bound on the plot, moves the amber and red segments between the 45 °C charging limit and the 60 °C discharging limit.

The mocked cycler replays a CC-CV charge to 54.6 V, a rest and a 75 A discharge of a 13S NMC, 50 Ah pack. Limits are typical for NMC cells: set yours from your cell datasheet.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/temperature.py` | The test |
| `plugs/cycler.py` | The cycler, mocked |
| `panels/temperature.html` | The panel |

## Run It

```bash
tofupilot run battery-temperature
```

Replace the mock in `plugs/cycler.py` with your cycler's and BMS's drivers to use it on a real bench.
