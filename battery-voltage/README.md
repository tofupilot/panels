# Pack Voltage

Pack voltage on a tape against the CV setpoint, red past the undervoltage and overvoltage limits.

See it live at [tofupilot.com/panels#battery-voltage](https://tofupilot.com/panels#battery-voltage).

## How It Works

`ui.voltage` fills a 36-60 V tape with `width: calc(...)`. The cyan mark is the 54.6 V CV setpoint (4.2 V per cell) and the red marks the 39.0 V undervoltage and 55.25 V overvoltage limits (3.0 and 4.25 V per cell); `ui.voltage_state` turns the tape red past them.

The mocked cycler replays a CC-CV charge to 54.6 V, a rest and a 75 A discharge of a 13S NMC, 50 Ah pack. Limits are typical for NMC cells: set yours from your cell datasheet.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/voltage.py` | The test |
| `plugs/cycler.py` | The cycler, mocked |
| `panels/voltage.html` | The panel |

## Run It

```bash
tofupilot run battery-voltage
```

Replace the mock in `plugs/cycler.py` with your cycler's and BMS's drivers to use it on a real bench.
