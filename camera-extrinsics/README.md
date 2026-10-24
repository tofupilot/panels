# Camera Extrinsics

The rig as the calibration places it in 3D, seen from behind the camera: the camera's field of view and each target at its measured position and tilt.

See it live at [tofupilot.com/panels#camera-extrinsics](https://tofupilot.com/panels#camera-extrinsics).

## How It Works

The value only exists in software, so this is a software view, not an instrument. The view is projected once, when the panel is written, from each target's pose in the calibration; `ui.poses` then reveals the targets one by one, each carrying its rank as `--k`. The station photos are generated scenes with real OpenCV patterns (cv2.aruco boards and markers) printed onto their plates; every corner, marker and pose drawn here is what OpenCV detected on them.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/camera_extrinsics.py` | The test |
| `plugs/pose_results.py` | The instrument, mocked |
| `panels/extrinsics.html` | The panel |

## Run It

```bash
tofupilot run camera-extrinsics
```

Replace the mock in `plugs/pose_results.py` with your calibration results's driver to use it on a real bench.
