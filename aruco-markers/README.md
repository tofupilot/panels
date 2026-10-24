# ArUco Markers

Six ArUco markers on a fixture plate: each one outlined as it is identified, then its pose drawn as three axes.

See it live at [tofupilot.com/panels#aruco-markers](https://tofupilot.com/panels#aruco-markers).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The photo is an image file next to the procedure (`images/aruco.jpg`). One group bound to `ui.step` reveals each marker's outline, then its red, green and blue pose axes, each carrying its rank as `--k`. The station photos are generated scenes with real OpenCV patterns (cv2.aruco boards and markers) printed onto their plates; every corner, marker and pose drawn here is what OpenCV detected on them.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/aruco_markers.py` | The test |
| `plugs/aruco_camera.py` | The instrument, mocked |
| `panels/markers.html` | The panel |

## Run It

```bash
tofupilot run aruco-markers
```

Replace the mock in `plugs/aruco_camera.py` with your station camera's driver to use it on a real bench.
