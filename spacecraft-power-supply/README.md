# Spacecraft Power Supply

The EGSE supply feeding a spacecraft's 28 V bus: voltage and current through switch-on, the inrush, and the load steps as subsystems power up.

See it live at [tofupilot.com/panels#spacecraft-power-supply](https://tofupilot.com/panels#spacecraft-power-supply).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. `ui.v0` to `ui.v3` and `ui.i0` to `ui.i3` drive the fluorescent 7-segment display. `ui.cv` and `ui.cc` show the regulation mode, `ui.limit` lights when the bus leaves its 22 to 36 V input range, and `ui.out` lights the output key.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/spacecraft_power_supply.py` | The test |
| `plugs/power_supply.py` | The instrument, mocked |
| `panels/supply.html` | The panel |

## Run It

```bash
tofupilot run spacecraft-power-supply
```

Replace the mock in `plugs/power_supply.py` with your egse power supply's driver to use it on a real bench.
