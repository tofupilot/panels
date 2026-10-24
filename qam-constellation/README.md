# 16-QAM Constellation

A vector signal analyzer's 16-QAM constellation while a power amplifier is tuned: the symbol clouds tighten around the ideal points as the error vector magnitude falls under its limit.

See it live at [tofupilot.com/panels#qam-constellation](https://tofupilot.com/panels#qam-constellation).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The constellation is a pool of 160 symbols, each a group inside a group: `ui.qi0` to `ui.qi159` move them along I and `ui.qq0` to `ui.qq159` along Q, on the -4 to 4 grid. Every update replaces the oldest 16. The ideal points are static.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/qam_constellation.py` | The test |
| `plugs/signal_analyzer.py` | The instrument, mocked |
| `panels/constellation.html` | The panel |

## Run It

```bash
tofupilot run qam-constellation
```

Replace the mock in `plugs/signal_analyzer.py` with your vector signal analyzer's driver to use it on a real bench.
