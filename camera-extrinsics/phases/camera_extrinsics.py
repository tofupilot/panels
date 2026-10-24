"""Reads each rig target's pose from the calibration: `ui.poses` reveals
the targets one by one in the 3D view. The run records the smallest tilt,
which must be large enough to measure the focal length, and the farthest
target."""
import time


def check_poses(ui, measurements, pose_results):
    results = pose_results.results()
    for _ in range(3):
        for index in range(len(results["tilts"])):
            ui.poses = index
            time.sleep(0.8)
        time.sleep(2.0)
        ui.poses = -1
        time.sleep(0.5)
    ui.poses = len(results["tilts"]) - 1
    measurements.min_tilt = min(results["tilts"])
    measurements.max_distance = max(results["distances"])
    time.sleep(2)
