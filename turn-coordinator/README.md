# Turn Coordinator

A turn coordinator: the aircraft banks onto the standard-rate mark with the turn rate, and the ball slips in its tube.

See it live at [tofupilot.com/panels#turn-coordinator](https://tofupilot.com/panels#turn-coordinator).

## How It Works

`ui.rate` banks the aircraft with `rotate()`, 20 degrees per 3 °/s, so a standard-rate turn puts its wing on L or R. The ball turns about the center of its curved tube by `ui.slip`, so it rides the curve instead of sliding in a straight line.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/turn_coordinator.py` | The test |
| `plugs/rate_table.py` | The instrument, mocked |
| `panels/turn.html` | The panel |

## Run It

```bash
tofupilot run turn-coordinator
```

Replace the mock in `plugs/rate_table.py` with your rate table's driver to use it on a real bench.
