# Bin Pareto

The fail bins of a 25-wafer lot as a pareto, the bars growing as each wafer is sorted: Vth and continuity fails at the edge lead, then leakage and the functional fails of the scratched wafers.

See it live at [tofupilot.com/panels#bin-pareto](https://tofupilot.com/panels#bin-pareto).

## How It Works

The value only exists in software, so this is a software view, not an instrument. Each bar is a group bound to its bin's fail count, `ui.b2` to `ui.b5`, scaled with `scaleY(calc(var(--value) / 300))` from its base. The bars are drawn in the order of the lot's final counts, so the chart reads as a pareto at the end of the lot.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/bin_pareto.py` | The test |
| `plugs/lot_tester.py` | The instrument, mocked |
| `panels/pareto.html` | The panel |

## Run It

```bash
tofupilot run bin-pareto
```

Replace the mock in `plugs/lot_tester.py` with your wafer sort tester's driver to use it on a real bench.
