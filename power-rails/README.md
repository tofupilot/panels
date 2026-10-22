# Power Rails Fixture

A board drawing whose test points light up as the probe moves, each turning green or red with its rail's result.

See it live at [tofupilot.com/panels#power-rails](https://tofupilot.com/panels#power-rails).

## How It Works

`ui.probe` names the test point under the probe, and the board's `data-value` rings it. Each rail is a measurement recorded as soon as it settles, so its pad turns green or red with `data-outcome` on the drawing.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/rails.py` | The test, with the instrument mocked |
| `panels/rails.html` | The panel |

## Run It

```bash
tofupilot run power-rails
```

Replace the mock in `phases/rails.py` with your instrument's driver to use it on a real bench.
