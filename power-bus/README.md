# Spacecraft Power Bus

The 28 V bus feeding a unit under test, against its 22 to 36 V input range, with the current drawn and the inrush at switch-on.

See it live at [tofupilot.com/panels#power-bus](https://tofupilot.com/panels#power-bus).

## How It Works

`ui.bus` fills a 20-40 V tape; the red marks are the 22 V and 36 V input range of a typical 28 V unit and the cyan mark is 28 V nominal. `ui.amps` shows the current drawn, including the inrush when the unit switches on, and `ui.bus_state` turns the tape red outside the input range.

Limits follow NASA GSFC-STD-7000B (GEVS) where it sets one; set yours from your test specification.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/power_bus.py` | The test |
| `plugs/power_supply.py` | The instrument, mocked |
| `panels/bus.html` | The panel |

## Run It

```bash
tofupilot run power-bus
```

Replace the mock in `plugs/power_supply.py` with your bus power supply's driver to use it on a real bench.
