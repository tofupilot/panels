# Charge and Discharge

The cycler software's plot of the run: pack voltage and current as the cycle goes, over the faint profile still to come.

See it live at [tofupilot.com/panels#battery-cycle](https://tofupilot.com/panels#battery-cycle).

## How It Works

The value only exists in software, so this is a software view, not an instrument. A panel has no script to draw a line, so the run is sixty points per trace: `ui.vh0` to `ui.vh59` and `ui.ih0` to `ui.ih59`, each sent once when the run reaches it and placed with `translate(var(--x), calc(...))` from its value. A point stays hidden until it has a value. The faint profile is drawn in the panel.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/battery_cycle.py` | The test |
| `plugs/cycler.py` | The instrument, mocked |
| `panels/cycle.html` | The panel |

## Run It

```bash
tofupilot run battery-cycle
```

Replace the mock in `plugs/cycler.py` with your battery cycler's driver to use it on a real bench.
