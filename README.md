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
| [Relay Matrix](relay-matrix) | A 4 x 16 switch matrix routing the meter node by node |
| [LED Color](led-color) | Eight LEDs dropping into their bins on the CIE 1931 diagram |
| [Bourdon Pressure Gauge](bourdon-gauge) | A Bourdon gauge with a drag pointer on a leak test |
| [Moving-Coil Ammeter](panel-ammeter) | A moving-coil ammeter with a mirror scale and a damped needle |
| [Chart Recorder](chart-recorder) | A two-pen paper chart recorder on a climatic chamber |
| [Force Gauge](force-gauge) | A force gauge on a connector insertion, with its force curve |
| [Electronic Load](electronic-load) | A DC electronic load discharging a lead-acid battery |
| [LED Level Meter](led-level-meter) | A two-channel LED level meter with peak hold |
| [Alarm Annunciator](alarm-annunciator) | An alarm annunciator with an ISA-18.1 first-out sequence |
| [Burn-in Heat Map](burn-in-heat-map) | A thermal camera's heat map over a KiCad board in burn-in |
| [USB 2.0 Eye and Mask](usb-eye-diagram) | A USB 2.0 eye with persistence against its mask |
| [Antenna Match on a Smith Chart](antenna-smith-chart) | An antenna's S11 sweep on a Smith chart as it is matched |
| [16-QAM Constellation](qam-constellation) | A 16-QAM constellation tightening as the amplifier is tuned |
| [I²C Logic Capture](i2c-logic-capture) | A logic analyzer decoding an I²C temperature read |
| [Calibration Rig](calibration-rig) | A camera calibration rig with every ChArUco target detected |
| [Chessboard Detection](chessboard-detection) | A chessboard's inner corners found row by row |
| [ChArUco Board](charuco-detection) | A ChArUco board's markers, corners and pose |
| [ArUco Markers](aruco-markers) | Six ArUco markers identified, each with its pose |
| [Reprojection Error](reprojection-error) | Reprojection error per target and every corner's residual |
| [Camera Extrinsics](camera-extrinsics) | The camera and each rig target's measured pose in 3D |
| [Wafer Map](wafer-map) | A wafer's bin map filling in as the probe card steps across it |
| [Probe Card Touchdown](probe-card-touchdown) | A multi-site probe card's sites colored by bin at every touchdown |
| [Parametric Wafer Map](parametric-wafer-map) | A heat map of each die's threshold voltage across the wafer |

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
