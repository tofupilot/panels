# State of Charge

The pack's state of charge as a battery outline that fills with the live SOC, with the cycler step next to it.

See it live at [tofupilot.com/panels#battery-soc](https://tofupilot.com/panels#battery-soc).

## How It Works

`ui.soc` sets `--value` on the battery body, and the fill's width is `calc(var(--value) * 1%)`. `ui.soc_state`, bound on the panel's root, turns the fill and the reading amber under 20 % and red under 10 % with `[data-value=warn]` and `[data-value=alarm]`.

The mocked cycler replays a CC-CV charge to 54.6 V, a rest and a 75 A discharge of a 13S NMC, 50 Ah pack. Limits are typical for NMC cells: set yours from your cell datasheet.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/soc.py` | The test |
| `plugs/cycler.py` | The cycler, mocked |
| `panels/soc.html` | The panel |

## Run It

```bash
tofupilot run battery-soc
```

Replace the mock in `plugs/cycler.py` with your cycler's and BMS's drivers to use it on a real bench.
