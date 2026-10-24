# ChArUco Board

A ChArUco board on a rotary stage: its ArUco markers found first, then the chessboard corners between them, then the board's pose as three axes.

See it live at [tofupilot.com/panels#charuco-detection](https://tofupilot.com/panels#charuco-detection).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The photo is an image file next to the procedure (`images/charuco.jpg`). One group bound to `ui.step` counts through the 17 markers, the 24 corners and the three pose axes, each carrying its rank as `--k`. The station photos are generated scenes with real OpenCV patterns (cv2.aruco boards and markers) printed onto their plates; every corner, marker and pose drawn here is what OpenCV detected on them.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/charuco_detection.py` | The test |
| `plugs/charuco_camera.py` | The instrument, mocked |
| `panels/detection.html` | The panel |

## Run It

```bash
tofupilot run charuco-detection
```

Replace the mock in `plugs/charuco_camera.py` with your station camera's driver to use it on a real bench.
