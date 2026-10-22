# Battery Pack Charge

State of charge, current, temperature and all eight cells live while a LiFePO4 pack charges and balances.

See it live at [tofupilot.com/panels#battery-charge](https://tofupilot.com/panels#battery-charge).

## How It Works

The pack's state of charge fills the battery shape with `height: calc(var(--value) * 1%)`. Each cell is a bar on `ui.cell_N`. The three results at the bottom bind measurements, so they turn green or red with `data-outcome` once recorded.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/charge.py` | The test, with the instrument mocked |
| `panels/charge.html` | The panel |

## Run It

```bash
tofupilot run battery-charge
```

Replace the mock in `phases/charge.py` with your instrument's driver to use it on a real bench.
