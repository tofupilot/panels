# Vacuum Gauge Controller

A thermal vacuum chamber's gauge controller through a pump-down: a full-range gauge and a Pirani that goes underrange, with the setpoint relays the test waits on.

See it live at [tofupilot.com/panels#vacuum-gauge](https://tofupilot.com/panels#vacuum-gauge).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. Each channel is six glyphs in E-notation, `ui.c1_0` to `ui.c1_5` and `ui.c2_0` to `ui.c2_5`; the 7-segment CSS includes E, U and r, so the Pirani can show `Ur` (underrange) once the chamber is below its range. `ui.sp1` and `ui.sp2` light the setpoint relays at 10 Pa and at the 1.33 × 10⁻³ Pa test vacuum of NASA GEVS.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/vacuum_gauge.py` | The test |
| `plugs/vacuum_gauge.py` | The instrument, mocked |
| `panels/gauge.html` | The panel |

## Run It

```bash
tofupilot run vacuum-gauge
```

Replace the mock in `plugs/vacuum_gauge.py` with your vacuum gauge controller's driver to use it on a real bench.
