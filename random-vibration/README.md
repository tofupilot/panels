# Random Vibration

The vibration controller's PSD screen through a run at −12, −6, −3 dB and full level: reference, ±3 dB tolerance and ±6 dB abort lines, and the control spectrum.

See it live at [tofupilot.com/panels#random-vibration](https://tofupilot.com/panels#random-vibration).

## How It Works

The value only exists in software, so this is a software view, not an instrument. `ui.level`, bound on the panel's root, shows the reference, ±3 dB tolerance and ±6 dB abort lines drawn for that level and lights the level steps. The control spectrum is 36 points, `ui.p0` to `ui.p35`, each the log10 of its ASD placed on the log-log grid; `ui.grms` is the control Grms. Full level is the GEVS component profile, 14.1 Grms.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/random_vibration.py` | The test |
| `plugs/shaker.py` | The instrument, mocked |
| `panels/vibration.html` | The panel |

## Run It

```bash
tofupilot run random-vibration
```

Replace the mock in `plugs/shaker.py` with your vibration controller's driver to use it on a real bench.
