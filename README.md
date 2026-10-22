# TofuPilot Panels

Example operator panels for [TofuPilot](https://tofupilot.com): custom test station screens written in plain HTML, CSS and inline SVG, bound to live measurements with `data-bind`. No JavaScript.

See them running live at [tofupilot.com/panels](https://tofupilot.com/panels), and learn how panels work in the [docs](https://tofupilot.com/docs/frameworks/tofupilot/operator-ui/panels).

| Example | Shows |
|---|---|
| [Airspeed Indicator](airspeed) | An SVG gauge with a needle on a live value, a red line, a button read by Python |
| [Battery Pack Charge](battery-charge) | State of charge, bars for eight cells, measurement results colored by their limits |
| [Power Rails Fixture](power-rails) | A board drawing whose test points light up with each rail's result |
| [Motor Spin Test](motor-spin) | Arc gauges and setpoint lights driven by CSS variables |
| [Cooling Fan Test](fan-test) | Looping CSS animations started and stopped by a live value |

## Run an Example

Every example runs on mocked instruments, so no hardware is needed.

```bash
curl -fsSL https://www.tofupilot.app/install | sh   # TofuPilot CLI 2.7.0 or newer
git clone https://github.com/tofupilot/panels
cd panels
tofupilot run airspeed
```

The run opens the operator UI in your browser with the panel live.

## Structure

```
<example>/
  procedure.yaml      # plugs, phases, measurements and limits, ui.panel
  phases/*.py         # the test
  plugs/*.py          # the instruments, mocked: replace them with your drivers
  panels/*.html       # the panel
  preview.json        # a recorded run, replayed on tofupilot.com/panels
panels.json           # the gallery's list: category, industry, minimum CLI, files
scripts/record.py     # runs an example and records preview.json
```

## Add an Example

1. Create a folder with `procedure.yaml`, `phases/`, `plugs/` and `panels/`, and check it passes with `tofupilot run <folder>`.
2. Add it to `panels.json`. `category` is what the panel shows (`gauges`, `indicators`, `bars`, `synoptics`, `alarms`, `inputs`, `animation`, `layout`); `industry` is one of the [industry pages](https://tofupilot.com/industries).
3. Record its preview with CLI 2.8.0 or newer: `pip install pyyaml && python scripts/record.py <folder>`.

The gallery shows a tagged release of this repository, so a new example appears on tofupilot.com once a release includes it.

## License

[MIT](LICENSE): copy the panels into your own procedures.
