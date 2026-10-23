# Digital Multimeter

A 6½-digit multimeter's display behind a scanner card, stepping through a board's four rails with each rail's ±3 % limit and verdict.

See it live at [tofupilot.com/panels#digital-multimeter](https://tofupilot.com/panels#digital-multimeter).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. The reading is seven 7-segment glyphs, `ui.v0` to `ui.v6`: a half digit then six full ones, as on the 10 V range. `ui.chn` names the channel, `ui.lim` the limit, and `ui.res` the verdict, colored by `[data-value=FAIL]`.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/digital_multimeter.py` | The test |
| `plugs/multimeter.py` | The instrument, mocked |
| `panels/multimeter.html` | The panel |

## Run It

```bash
tofupilot run digital-multimeter
```

Replace the mock in `plugs/multimeter.py` with your multimeter's driver to use it on a real bench.
