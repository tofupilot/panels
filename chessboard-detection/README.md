# Chessboard Detection

A chessboard target on a tilt stage, its 9 x 6 inner corners found row by row and joined the way OpenCV draws them.

See it live at [tofupilot.com/panels#chessboard-detection](https://tofupilot.com/panels#chessboard-detection).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The photo is an image file next to the procedure (`images/chessboard.jpg`). One group bound to `ui.found` counts the corners: each corner and the segment that reaches it carry their rank as `--k`, colored by row. The station photos are generated scenes with real OpenCV patterns (cv2.aruco boards and markers) printed onto their plates; every corner, marker and pose drawn here is what OpenCV detected on them.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/chessboard_detection.py` | The test |
| `plugs/chessboard_camera.py` | The instrument, mocked |
| `panels/detection.html` | The panel |

## Run It

```bash
tofupilot run chessboard-detection
```

Replace the mock in `plugs/chessboard_camera.py` with your station camera's driver to use it on a real bench.
