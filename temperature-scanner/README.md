# Temperature Scanner

An 8-channel thermocouple scanner on the cells, the busbar and the coolant, with each channel's alarm against the limit of the step being run.

See it live at [tofupilot.com/panels#temperature-scanner](https://tofupilot.com/panels#temperature-scanner).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. Each channel is three 7-segment digits, `ui.t1_0` to `ui.t8_2`. `ui.a1` to `ui.a8` show HI or ALM against the limit of the step, 45 °C while charging and 60 °C while discharging, amber 5 °C before; `ui.mode` names the limit in force.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/temperature_scanner.py` | The test |
| `plugs/scanner.py` | The instrument, mocked |
| `panels/scanner.html` | The panel |

## Run It

```bash
tofupilot run temperature-scanner
```

Replace the mock in `plugs/scanner.py` with your temperature scanner's driver to use it on a real bench.
