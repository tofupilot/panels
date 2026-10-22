# TofuPilot Panels

Example operator panels for [TofuPilot](https://tofupilot.com): custom test station screens written in plain HTML, CSS and inline SVG, bound to live measurements with `data-bind`. No JavaScript.

See them running live at [tofupilot.com/panels](https://tofupilot.com/panels), and learn how panels work in the [docs](https://tofupilot.com/docs/frameworks/tofupilot/operator-ui/panels).

| Example | Shows |
|---|---|
| [Airspeed Indicator](airspeed) | An SVG arc that sweeps with a live value and turns red past a red line |
| [Attitude Indicator](attitude) | A horizon that pitches and banks behind a fixed aircraft symbol |
| [Altimeter](altimeter) | An arc that sweeps to the live altitude, with a bug on the selected one |
| [Turn Coordinator](turn-coordinator) | An aircraft that banks with the turn rate, and a slip ball |
| [Heading Indicator](heading) | A compass card that turns under the lubber line, with a heading bug |
| [Vertical Speed Indicator](vertical-speed) | An arc that fills up in a climb, down in a descent, red past a sink limit |
| [TVAC Chamber Pressure](tvac-pressure) | Chamber pressure on a log scale, with the test vacuum line |
| [TVAC Thermal Cycle](tvac-cycle) | Baseplate temperature against the plateau setpoints and ±2 °C band |
| [Random Vibration](random-vibration) | Control Grms against the reference, stepping up to full level |
| [Spacecraft Power Bus](power-bus) | The 28 V bus against the unit's input range, with the current drawn |
| [RF Link Acquisition](rf-link) | Carrier, bit sync and frame sync locks, and Eb/N0 against threshold |
| [State of Charge](battery-soc) | A battery outline that fills with the live SOC |
| [Pack Current](battery-current) | A center-zero current tape with charge and discharge limits |
| [Max Temperature](battery-temperature) | Eight thermistors on one scale, limits that follow the mode |
| [Cell Voltage Balance](cell-balance) | Thirteen cells as deviation from the mean, with balancing lights |
| [Pack Voltage](battery-voltage) | A pack voltage tape with the CV setpoint and UV/OV limits |

## Run an Example

Every example runs on mocked instruments, so no hardware is needed.

```bash
curl -fsSL https://www.tofupilot.app/install | sh   # TofuPilot CLI 2.8.0 or newer
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
