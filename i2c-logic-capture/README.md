# I²C Logic Capture

A logic analyzer capturing a TMP117 temperature read on I²C: SCL and SDA drawn as the capture sweeps across, the decoded address, register and data bytes above, and the temperature they encode.

See it live at [tofupilot.com/panels#i2c-logic-capture](https://tofupilot.com/panels#i2c-logic-capture).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The waveform and its decode are drawn once from the transaction; `ui.sweep`, from 0 to 1, slides a cover off them with `scaleX(...)` as the capture comes in. `ui.temp` is the decoded temperature.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/i2c_logic_capture.py` | The test |
| `plugs/logic_analyzer.py` | The instrument, mocked |
| `panels/capture.html` | The panel |

## Run It

```bash
tofupilot run i2c-logic-capture
```

Replace the mock in `plugs/logic_analyzer.py` with your logic analyzer's driver to use it on a real bench.
