# Cell Voltage Balance

The 13 cells as the BMS view shows them: each cell's deviation from the pack mean, the cells being balanced, and the spread against its limits.

See it live at [tofupilot.com/panels#cell-balance](https://tofupilot.com/panels#cell-balance).

## How It Works

The value only exists in software, so this is a software view, not an instrument. Each of `ui.d1` to `ui.d13` is a cell's deviation from the mean in mV. A bar of 46 units is scaled with `scaleY(clamp(-1, var(--value) / 60, 1))` from its bottom edge on the center line, so a negative value flips it below the line. `ui.b1` to `ui.b13` light the cyan balancing dots; `ui.cell_state` colors the bars amber past 50 mV and red past 100 mV.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/cell_balance.py` | The test |
| `plugs/cycler.py` | The instrument, mocked |
| `panels/balance.html` | The panel |

## Run It

```bash
tofupilot run cell-balance
```

Replace the mock in `plugs/cycler.py` with your battery cycler's driver to use it on a real bench.
