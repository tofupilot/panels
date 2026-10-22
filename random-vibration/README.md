# Random Vibration

A random vibration run stepping −12, −6, −3 dB to full level, with the control Grms against the reference and its ±10 % tolerance band.

See it live at [tofupilot.com/panels#random-vibration](https://tofupilot.com/panels#random-vibration).

## How It Works

`ui.level` lights the level steps with attribute selectors (`[data-value="-6"]` and so on). `ui.grms` fills a 0-20 Grms tape and `ui.reference` places the ±10 % band, the GEVS random vibration RMS tolerance, around the reference of the current level: 14.1 Grms at full level, the GEVS component example. `ui.vibe_state` turns the tape red outside the band.

Limits follow NASA GSFC-STD-7000B (GEVS) where it sets one; set yours from your test specification.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/random_vibration.py` | The test |
| `plugs/shaker.py` | The instrument, mocked |
| `panels/random.html` | The panel |

## Run It

```bash
tofupilot run random-vibration
```

Replace the mock in `plugs/shaker.py` with your shaker controller's driver to use it on a real bench.
