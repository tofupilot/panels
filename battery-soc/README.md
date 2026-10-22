# State of Charge

State of charge as the cycler's software shows it: a large reading, twenty segments that go amber then red when low, and the charge moved so far.

See it live at [tofupilot.com/panels#battery-soc](https://tofupilot.com/panels#battery-soc).

## How It Works

The value only exists in software, so this is a software view, not an instrument. SOC is an estimate from the coulomb count, so it lives in software, not on an instrument. Each of the twenty segments sets its own opacity from `ui.soc` with `clamp(.13, var(--value) - 5k, 1)`: lit once SOC passes it. `ui.soc_state` turns them amber under 20 % and red under 10 %.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/battery_soc.py` | The test |
| `plugs/cycler.py` | The instrument, mocked |
| `panels/soc.html` | The panel |

## Run It

```bash
tofupilot run battery-soc
```

Replace the mock in `plugs/cycler.py` with your battery cycler's driver to use it on a real bench.
