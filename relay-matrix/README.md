# Relay Matrix

A 4 x 16 crosspoint switch matrix routing a multimeter to a board's test nodes one at a time: ABUS1 to the node, ABUS2 to ground, each closed crosspoint lit.

See it live at [tofupilot.com/panels#relay-matrix](https://tofupilot.com/panels#relay-matrix).

## How It Works

The value only exists in software, so this is a software view, not an instrument. Each crosspoint is a group bound to `ui.x{bus}_{column}`, from `ui.x0_0` to `ui.x3_15`; `[data-value=true]` lights the closed ones. The phase closes ABUS1 on the node and ABUS2 on ground, reads the meter, then opens both.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/relay_matrix.py` | The test |
| `plugs/switch_matrix.py` | The instrument, mocked |
| `panels/matrix.html` | The panel |

## Run It

```bash
tofupilot run relay-matrix
```

Replace the mock in `plugs/switch_matrix.py` with your switch matrix's driver to use it on a real bench.
