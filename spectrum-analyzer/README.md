# Spectrum Analyzer

The RF checkout spectrum analyzer on a spacecraft's S-band downlink: the noise floor, then the QPSK carrier rising out of it, with the marker on the peak.

See it live at [tofupilot.com/panels#spectrum-analyzer](https://tofupilot.com/panels#spectrum-analyzer).

## How It Works

It is the front panel of the instrument itself, drawn as hardware. The trace is 48 points, `ui.s0` to `ui.s47` in dBm, each placed with `translate(var(--x), calc(...))` on the 10 dB/div screen. The marker is a group inside a group: `ui.pk` moves it across to the peak's bin and `ui.pl` down to its level; `ui.mkr` is the marker readout.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/spectrum_analyzer.py` | The test |
| `plugs/spectrum_analyzer.py` | The instrument, mocked |
| `panels/analyzer.html` | The panel |

## Run It

```bash
tofupilot run spectrum-analyzer
```

Replace the mock in `plugs/spectrum_analyzer.py` with your spectrum analyzer's driver to use it on a real bench.
