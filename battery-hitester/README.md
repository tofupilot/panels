# Battery HiTester

An AC internal resistance meter on the pack: resistance at 1 kHz and voltage on a reflective LCD, with the HI, IN and LO comparator lamps.

See it live at [tofupilot.com/panels#battery-hitester](https://tofupilot.com/panels#battery-hitester).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. `ui.r0` to `ui.r3` and `ui.v0` to `ui.v5` drive the LCD's 7-segment digits. `ui.comp`, bound on the lamp group, lights HI, IN or LO with `[data-value=IN]` and so on, against the 8.0 to 12.0 mΩ window.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/battery_hitester.py` | The test |
| `plugs/hitester.py` | The instrument, mocked |
| `panels/hitester.html` | The panel |

## Run It

```bash
tofupilot run battery-hitester
```

Replace the mock in `plugs/hitester.py` with your battery hitester's driver to use it on a real bench.
