# TofuPilot Panels

Example operator panels for [TofuPilot](https://tofupilot.com): custom test station screens written in plain HTML, CSS and inline SVG, bound to live measurements with `data-bind`. No JavaScript.

See them running live at [tofupilot.com/panels](https://tofupilot.com/panels), and learn how panels work in the [docs](https://tofupilot.com/docs/frameworks/tofupilot/operator-ui/panels).

| Example | Shows |
|---|---|
| [Airspeed Indicator](airspeed) | An SVG gauge with a needle on a live value, a red line, a button read by Python |
| [Battery Pack Charge](battery-charge) | State of charge, bars for eight cells, measurement results colored by their limits |
| [Power Rails Fixture](power-rails) | A board drawing whose test points light up with each rail's result |
| [Motor Spin Test](motor-spin) | Arc gauges and setpoint lights driven by CSS variables |

## Run an Example

Every example runs on mocked instruments, so no hardware is needed.

```bash
curl -fsSL https://www.tofupilot.app/install | sh   # install the TofuPilot CLI
git clone https://github.com/tofupilot/panels
cd panels
tofupilot run airspeed
```

The run opens the operator UI in your browser with the panel live.

## Structure

```
<example>/
  procedure.yaml      # phases, measurements and limits, ui.panel
  phases/*.py         # the test, with the instrument mocked
  panels/*.html       # the panel
  preview.json        # a recorded run, replayed on tofupilot.com/panels
panels.json           # the gallery's list of examples
scripts/record.py     # runs an example and records preview.json
```

## Add an Example

1. Create a folder with `procedure.yaml`, `phases/` and `panels/`, and check it passes with `tofupilot run <folder>`.
2. Add it to `panels.json`.
3. Record its preview: `pip install pyyaml && python scripts/record.py <folder>`.

The gallery picks up new examples within the hour.
