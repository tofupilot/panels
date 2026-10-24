# LED Level Meter

A two-channel LED level meter on an amplifier's outputs while a 1 kHz tone steps up to the +4 dBu nominal level: green below 0 dBu, amber to +6, red above, with a peak-hold segment.

See it live at [tofupilot.com/panels#led-level-meter](https://tofupilot.com/panels#led-level-meter).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. Each channel is a group bound to its level, `ui.l` or `ui.r` in dBu, holding a group bound to its peak, `ui.lp` or `ui.rp`. Every segment lights with `opacity: clamp(0, (var(--lv) - level) * 99, 1)`, and the segment at the held peak with the same test on `--pk`. 

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/led_level_meter.py` | The test |
| `plugs/audio_analyzer.py` | The instrument, mocked |
| `panels/meter.html` | The panel |

## Run It

```bash
tofupilot run led-level-meter
```

Replace the mock in `plugs/audio_analyzer.py` with your audio analyzer's driver to use it on a real bench.
