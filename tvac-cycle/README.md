# TVAC Thermal Cycle

A thermal vacuum cycle: the baseplate temperature against the cold and hot plateau setpoints, with the ±2 °C tolerance band and the dwell time.

See it live at [tofupilot.com/panels#tvac-cycle](https://tofupilot.com/panels#tvac-cycle).

## How It Works

`ui.temp` fills a -50 to +80 °C tape. `ui.target` places a cyan ±2 °C band on the plateau being run, the GEVS temperature tolerance, and the cyan marks are the -30 °C and +60 °C plateau setpoints. `ui.cycle_state` turns the tape amber when the baseplate leaves the band during a dwell. `ui.stage` shows the step and the dwell time.

Limits follow NASA GSFC-STD-7000B (GEVS) where it sets one; set yours from your test specification.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/tvac_cycle.py` | The test |
| `plugs/thermal_controller.py` | The instrument, mocked |
| `panels/cycle.html` | The panel |

## Run It

```bash
tofupilot run tvac-cycle
```

Replace the mock in `plugs/thermal_controller.py` with your thermal controller's driver to use it on a real bench.
