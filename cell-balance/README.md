# Cell Voltage Balance

Each of 13 cells as its deviation from the pack mean in mV, with balancing lights and the spread against its limits.

See it live at [tofupilot.com/panels#cell-balance](https://tofupilot.com/panels#cell-balance).

## How It Works

Each of `ui.d1` to `ui.d13` is a cell's deviation from the mean in mV. A bar grows up or down from the center line: its height is `max(var(--value), var(--value) * -1)` and a negative bar is moved below the line with `translateY()`. `ui.b1` to `ui.b13` light the cyan dots while a cell is balanced.

The mocked cycler replays a CC-CV charge to 54.6 V, a rest and a 75 A discharge of a 13S NMC, 50 Ah pack. Limits are typical for NMC cells: set yours from your cell datasheet.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/cells.py` | The test |
| `plugs/cycler.py` | The cycler, mocked |
| `panels/cells.html` | The panel |

## Run It

```bash
tofupilot run cell-balance
```

Replace the mock in `plugs/cycler.py` with your cycler's and BMS's drivers to use it on a real bench.
