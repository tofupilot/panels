# RF Link Acquisition

Downlink acquisition on the RF checkout equipment: carrier, bit sync and frame sync locks in order, and Eb/N0 against the 9.6 dB BPSK threshold.

See it live at [tofupilot.com/panels#rf-link](https://tofupilot.com/panels#rf-link).

## How It Works

`ui.carrier`, `ui.bit_sync` and `ui.frame_sync` light the three locks in the order a receiver acquires them. `ui.ebn0` fills a 0-20 dB tape; the amber mark is 9.6 dB, the Eb/N0 uncoded BPSK needs for a bit error rate of 10⁻⁵, and `ui.link_state` turns the reading amber below it once the receiver is locked.

Limits follow NASA GSFC-STD-7000B (GEVS) where it sets one; set yours from your test specification.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/rf_link.py` | The test |
| `plugs/rf_scoe.py` | The instrument, mocked |
| `panels/link.html` | The panel |

## Run It

```bash
tofupilot run rf-link
```

Replace the mock in `plugs/rf_scoe.py` with your rf checkout equipment's driver to use it on a real bench.
