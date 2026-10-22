# Thermal Controller

A thermal vacuum chamber's programmer running one protoflight cycle on a unit's baseplate: process value in red, setpoint in green, heat and LN2 outputs, and the deviation alarm.

See it live at [tofupilot.com/panels#thermal-controller](https://tofupilot.com/panels#thermal-controller).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. `ui.pv0` to `ui.pv3` and `ui.sv0` to `ui.sv3` drive the red and green 7-segment displays. `ui.op1` and `ui.op2` light the heat and LN2 outputs, `ui.al1` the deviation alarm when the baseplate leaves ±2 °C (GEVS) during a dwell, and `ui.prog` names the program segment.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/thermal_controller.py` | The test |
| `plugs/thermal_controller.py` | The instrument, mocked |
| `panels/controller.html` | The panel |

## Run It

```bash
tofupilot run thermal-controller
```

Replace the mock in `plugs/thermal_controller.py` with your thermal controller's driver to use it on a real bench.
