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
| [Battery Cycler Channel](battery-cycler) | A cycler channel's front panel: V, A, CC/CV and overcurrent |
| [Battery HiTester](battery-hitester) | An AC-IR meter's LCD with its HI / IN / LO comparator |
| [Temperature Scanner](temperature-scanner) | An 8-channel thermocouple scanner with per-channel alarms |
| [State of Charge](battery-soc) | SOC as twenty segments, with the charge moved |
| [Cell Voltage Balance](cell-balance) | Thirteen cells as deviation from the mean, with balancing |
| [Charge and Discharge](battery-cycle) | The cycler software's voltage and current plot of the run |
| [Vacuum Gauge Controller](vacuum-gauge) | A two-channel vacuum gauge controller with setpoint relays |
| [Thermal Controller](thermal-controller) | A chamber programmer's PV and SV through a thermal cycle |
| [Spectrum Analyzer](spectrum-analyzer) | A spectrum analyzer's screen on the downlink carrier, with its marker |
| [Spacecraft Power Supply](spacecraft-power-supply) | The EGSE supply on the 28 V bus: V, A, CV/CC and the limit lamp |
| [Random Vibration](random-vibration) | The vibration controller's PSD through the level steps |
| [Reaction Wheels](reaction-wheels) | Four reaction wheels from telemetry on center-zero bars |
| [Digital Multimeter](digital-multimeter) | A 6½-digit multimeter scanning a board's rails |
| [Triple-Output Power Supply](triple-power-supply) | A triple-output supply's display with CV and CC per channel |
| [Oscilloscope](oscilloscope) | A 4-channel scope screen on a board's power-up sequence |
| [Test Point Probing](test-point-probing) | A KiCad board's test points probed one by one |
| [Board View](board-view) | A KiCad board's parts lit step by step by the functional test |

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
