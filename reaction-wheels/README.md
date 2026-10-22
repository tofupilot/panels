# Reaction Wheels

Reaction wheel speeds from spacecraft telemetry during an attitude control test: four wheels in a pyramid on center-zero bars, amber near saturation, red past it.

See it live at [tofupilot.com/panels#reaction-wheels](https://tofupilot.com/panels#reaction-wheels).

## How It Works

The value only exists in software, so this is a software view, not an instrument. Wheel speeds come from telemetry, so there is no instrument: this is a software view. Each bar is half the track wide, anchored at zero and scaled with `scaleX(clamp(-1, var(--value) / 6000, 1))` from its left edge, so a negative speed flips it left. `ui.rw1s` to `ui.rw4s` color each row amber past 5000 rpm and red past 5500 rpm.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/reaction_wheels.py` | The test |
| `plugs/telemetry.py` | The instrument, mocked |
| `panels/wheels.html` | The panel |

## Run It

```bash
tofupilot run reaction-wheels
```

Replace the mock in `plugs/telemetry.py` with your spacecraft telemetry's driver to use it on a real bench.
