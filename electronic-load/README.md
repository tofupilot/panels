# Electronic Load

A DC electronic load discharging a 12 V, 7.2 Ah lead-acid battery at C/10 in constant current down to the 10.5 V cutoff: volts, amps, watts, amp-hours and elapsed time.

See it live at [tofupilot.com/panels#electronic-load](https://tofupilot.com/panels#electronic-load).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. Each readout is one bound value, formatted by the phase: `ui.v`, `ui.a`, `ui.w`, `ui.ah` and `ui.time`. The mode, the set current and the cutoff are part of the display.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/electronic_load.py` | The test |
| `plugs/electronic_load.py` | The instrument, mocked |
| `panels/load.html` | The panel |

## Run It

```bash
tofupilot run electronic-load
```

Replace the mock in `plugs/electronic_load.py` with your electronic load's driver to use it on a real bench.
