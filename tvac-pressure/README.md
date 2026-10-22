# TVAC Chamber Pressure

Thermal vacuum chamber pressure on a log scale from atmosphere to high vacuum, with the 1.33 × 10⁻³ Pa test vacuum line.

See it live at [tofupilot.com/panels#tvac-pressure](https://tofupilot.com/panels#tvac-pressure).

## How It Works

The phase sends `ui.decades`, the pressure as decades below atmosphere (`5 - log10(Pa)`), and the tape fills with `calc(var(--value) / 10 * 100%)`; a log scale needs no JavaScript that way. `ui.pressure` is the reading already formatted with its power of ten. The cyan mark is the 1.33 × 10⁻³ Pa (1 × 10⁻⁵ torr) test vacuum of NASA GEVS; `ui.at_vacuum` turns the reading green once the chamber is below it.

Limits follow NASA GSFC-STD-7000B (GEVS) where it sets one; set yours from your test specification.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/tvac_pressure.py` | The test |
| `plugs/vacuum_gauge.py` | The instrument, mocked |
| `panels/pressure.html` | The panel |

## Run It

```bash
tofupilot run tvac-pressure
```

Replace the mock in `plugs/vacuum_gauge.py` with your vacuum gauge's driver to use it on a real bench.
