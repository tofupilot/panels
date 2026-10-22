# Pack Current

Pack current on a center-zero tape: charge fills right, discharge fills left, red past the charge and discharge limits.

See it live at [tofupilot.com/panels#battery-current](https://tofupilot.com/panels#battery-current).

## How It Works

`ui.current` drives two fills from the center: `clamp(0, var(--value), 100)` to the right for charge and `clamp(0, var(--value) * -1, 100)` to the left for discharge, so only one shows at a time, and a pointer placed with `left: calc(...)`. The red marks are the -85 A and +60 A limits; `ui.current_state` turns the tape red past them.

The mocked cycler replays a CC-CV charge to 54.6 V, a rest and a 75 A discharge of a 13S NMC, 50 Ah pack. Limits are typical for NMC cells: set yours from your cell datasheet.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/current.py` | The test |
| `plugs/cycler.py` | The cycler, mocked |
| `panels/current.html` | The panel |

## Run It

```bash
tofupilot run battery-current
```

Replace the mock in `plugs/cycler.py` with your cycler's and BMS's drivers to use it on a real bench.
