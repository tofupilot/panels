# Moving-Coil Ammeter

A moving-coil DC panel ammeter, 0 to 5 A on a 90° scale with a mirror band, reading a product's supply current as its stages switch on; the needle overshoots and settles like a damped movement.

See it live at [tofupilot.com/panels#panel-ammeter](https://tofupilot.com/panels#panel-ammeter).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. The needle is a group bound to `ui.amps`, turned with `rotate(calc(-45deg + var(--value) * 18deg))` around its pivot. Its transition uses an overshooting cubic-bezier, so each new reading swings past and settles, the way a damped movement does.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/panel_ammeter.py` | The test |
| `plugs/load_ammeter.py` | The instrument, mocked |
| `panels/ammeter.html` | The panel |

## Run It

```bash
tofupilot run panel-ammeter
```

Replace the mock in `plugs/load_ammeter.py` with your panel ammeter's driver to use it on a real bench.
