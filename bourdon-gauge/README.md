# Bourdon Pressure Gauge

A Bourdon tube gauge on a pressure-decay leak test: the part fills to 6 bar, settles and holds while the decay is measured, then vents, with the red drag pointer keeping the peak.

See it live at [tofupilot.com/panels#bourdon-gauge](https://tofupilot.com/panels#bourdon-gauge).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. The needle is a group bound to `ui.bar`, turned with `rotate(calc(-135deg + var(--value) * 27deg))` around the dial's centre; the red drag pointer is the same on `ui.peak`. The 0-10 bar dial, the red band and the ticks are fixed SVG.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/bourdon_gauge.py` | The test |
| `plugs/leak_tester.py` | The instrument, mocked |
| `panels/gauge.html` | The panel |

## Run It

```bash
tofupilot run bourdon-gauge
```

Replace the mock in `plugs/leak_tester.py` with your leak tester's driver to use it on a real bench.
