# Test Point Probing

A board's bottom side drawn from its KiCad layout, with a bed-of-nails fixture probing its 19 test points in turn: each one turns green within its level or red outside it, and the probe shows the net and the reading.

See it live at [tofupilot.com/panels#test-point-probing](https://tofupilot.com/panels#test-point-probing).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The board is SVG exported from the KiCad layout and kept under the panel size limit. Each test point is a group bound to `ui.tp1` to `ui.tp19`, green for `pass`, red for `fail`. The probe is a group inside a group: `ui.px` and `ui.py` move it, `ui.tag` is its label and `ui.side` flips the label left near the edge. The board is the GreatFET One by Great Scott Gadgets (BSD-3-Clause), drawn from its KiCad layout (github.com/greatscottgadgets/greatfet-hardware, azalea).

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/test_point_probing.py` | The test |
| `plugs/fixture.py` | The instrument, mocked |
| `panels/probing.html` | The panel |

## Run It

```bash
tofupilot run test-point-probing
```

Replace the mock in `plugs/fixture.py` with your in-circuit fixture's driver to use it on a real bench.
