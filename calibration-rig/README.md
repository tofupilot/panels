# Calibration Rig

A fixed camera on an end-of-line calibration rig: four ChArUco targets tilted on an aluminium frame, their markers then their corners detected target by target, ending in the camera's calibration.

See it live at [tofupilot.com/panels#calibration-rig](https://tofupilot.com/panels#calibration-rig).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The photo is an image file next to the procedure (`images/rig.jpg`), drawn in the panel's SVG. Each target is a group bound to `ui.t1` to `ui.t4`, a count: every marker outline and corner carries its rank as `--k` and shows once the count passes it. The station photos are generated scenes with real OpenCV patterns (cv2.aruco boards and markers) printed onto their plates; every corner, marker and pose drawn here is what OpenCV detected on them.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/calibration_rig.py` | The test |
| `plugs/rig_camera.py` | The instrument, mocked |
| `panels/rig.html` | The panel |

## Run It

```bash
tofupilot run calibration-rig
```

Replace the mock in `plugs/rig_camera.py` with your station camera's driver to use it on a real bench.
