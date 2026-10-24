# Alarm Annunciator

A test station's alarm annunciator through one incident: LOW AIR comes in first and flashes fast, VAC LOSS follows and flashes slow, both turn steady once acknowledged, then clear.

See it live at [tofupilot.com/panels#alarm-annunciator](https://tofupilot.com/panels#alarm-annunciator).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. Each window is a group bound to its alarm, `ui.low_air` and so on. `[data-value=first]` lights it with a fast flash (the first-out), `[data-value=new]` with a slow one, `[data-value=on]` steady; an empty value leaves it dark. The flashing is a CSS animation, so the phase only sends state changes.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/alarm_annunciator.py` | The test |
| `plugs/annunciator.py` | The instrument, mocked |
| `panels/annunciator.html` | The panel |

## Run It

```bash
tofupilot run alarm-annunciator
```

Replace the mock in `plugs/annunciator.py` with your alarm annunciator's driver to use it on a real bench.
