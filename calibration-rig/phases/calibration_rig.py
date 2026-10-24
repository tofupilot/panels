"""Detects the four ChArUco targets of the rig, then calibrates the camera.
`ui.t1` to `ui.t4` reveal each target's detections in the order OpenCV
found them: its markers, then its corners. The run records the reprojection
error and the focal length of the calibration."""
import time


def calibrate(ui, measurements, rig_camera):
    results = rig_camera.results()
    for index, (markers, corners) in enumerate(results["targets"], 1):
        total = markers + corners
        for shown in range(0, total + 8, 8):
            setattr(ui, f"t{index}", min(shown, total))
            time.sleep(0.1)
        time.sleep(0.4)
    measurements.reprojection_rms = results["rms"]
    measurements.focal_length = results["fx"]
    time.sleep(2.5)
