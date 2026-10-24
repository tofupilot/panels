# Twelve-Slot Fixture

A 12-slot fixture testing boards in parallel: slots start one after another, each fills its progress bar, one goes amber for a retest, and all finish green.

See it live at [tofupilot.com/panels#twelve-slot-fixture](https://tofupilot.com/panels#twelve-slot-fixture).

## How It Works

The value only exists in software, so this is a software view, not an instrument. Each slot is two bound values: `ui.s0` to `ui.s11`, its state (wait, run, retest, pass) colouring the tile and its lamp with `[data-value=run]` and so on, and `ui.p0` to `ui.p11`, its progress as a `scaleX(...)` bar.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/twelve_slot_fixture.py` | The test |
| `plugs/fixture_controller.py` | The instrument, mocked |
| `panels/fixture.html` | The panel |

## Run It

```bash
tofupilot run twelve-slot-fixture
```

Replace the mock in `plugs/fixture_controller.py` with your fixture controller's driver to use it on a real bench.
