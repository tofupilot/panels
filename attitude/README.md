# Attitude Indicator

An attitude indicator: the horizon pitches and banks behind a fixed aircraft symbol while a tilt table moves the unit.

See it live at [tofupilot.com/panels#attitude](https://tofupilot.com/panels#attitude).

## How It Works

`ui.roll` turns the horizon about the dial's center with `rotate()`, and `ui.pitch`, bound on a group inside it, slides the sky, the ground and the pitch ladder with `translateY()`, 2.2 units per degree. A `clipPath` keeps them inside the face. The aircraft symbol and the bank scale do not move; the sky pointer turns with the horizon.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/attitude.py` | The test |
| `plugs/tilt_table.py` | The instrument, mocked |
| `panels/attitude.html` | The panel |

## Run It

```bash
tofupilot run attitude
```

Replace the mock in `plugs/tilt_table.py` with your tilt table's driver to use it on a real bench.
