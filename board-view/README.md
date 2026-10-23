# Board View

A board's top side drawn from its KiCad layout, the way an interactive BOM shows it: each step of the functional test lights the parts it checks and names the result.

See it live at [tofupilot.com/panels#board-view](https://tofupilot.com/panels#board-view).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The board is SVG exported from the KiCad layout. Every part a step checks is a box; `ui.step`, bound on the panel's root, picks which boxes light with `.inst[data-value='3'] .c-U2` and where the label goes. `ui.tag` is the label and `ui.ok` turns the highlight red when a check fails. The board is the GreatFET One by Great Scott Gadgets (BSD-3-Clause), drawn from its KiCad layout (github.com/greatscottgadgets/greatfet-hardware, azalea).

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/board_view.py` | The test |
| `plugs/board_tester.py` | The instrument, mocked |
| `panels/view.html` | The panel |

## Run It

```bash
tofupilot run board-view
```

Replace the mock in `plugs/board_tester.py` with your board tester's driver to use it on a real bench.
