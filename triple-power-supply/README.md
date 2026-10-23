# Triple-Output Power Supply

A triple-output supply's display as its channels switch on: set point, volts, amps and watts per channel, and the CV or CC badge when a current limit is reached.

See it live at [tofupilot.com/panels#triple-power-supply](https://tofupilot.com/panels#triple-power-supply).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. Each channel is three bound readouts, `ui.v1`, `ui.a1` and `ui.w1` for channel 1, and a mode, `ui.m1`. The mode is both the badge's text and its color: `[data-value=CC]` turns it red, `[data-value=OFF]` dims the tile.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/triple_power_supply.py` | The test |
| `plugs/power_supply_3ch.py` | The instrument, mocked |
| `panels/supply.html` | The panel |

## Run It

```bash
tofupilot run triple-power-supply
```

Replace the mock in `plugs/power_supply_3ch.py` with your triple-output power supply's driver to use it on a real bench.
