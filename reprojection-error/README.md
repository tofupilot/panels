# Reprojection Error

The calibration's reprojection error: one bar per rig target against the 0.5 px limit, and every corner's residual in a scatter around zero.

See it live at [tofupilot.com/panels#reprojection-error](https://tofupilot.com/panels#reprojection-error).

## How It Works

The value only exists in software, so this is a software view, not an instrument. Each bar is a group bound to `ui.e1` to `ui.e4`, the target's RMS in pixels, scaled with `scaleY(var(--value))`. The 216 residuals are pre-placed points revealed target by target by `ui.shown`. Both come from the real OpenCV calibration of the rig photo. The station photos are generated scenes with real OpenCV patterns (cv2.aruco boards and markers) printed onto their plates; every corner, marker and pose drawn here is what OpenCV detected on them.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/reprojection_error.py` | The test |
| `plugs/calibration_results.py` | The instrument, mocked |
| `panels/error.html` | The panel |

## Run It

```bash
tofupilot run reprojection-error
```

Replace the mock in `plugs/calibration_results.py` with your calibration results's driver to use it on a real bench.
