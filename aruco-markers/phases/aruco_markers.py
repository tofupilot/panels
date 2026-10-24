"""Identifies the six ArUco markers on the fixture plate and estimates each
one's pose: `ui.step` reveals each outline, then its axes. The run records
how many markers it identified."""
import time


def find_markers(ui, measurements, aruco_camera):
    results = aruco_camera.results()
    total = 2 * len(results["ids"])
    for _ in range(3):
        for step in range(total + 1):
            ui.step = step
            time.sleep(0.35)
        time.sleep(1.5)
        ui.step = -1
        time.sleep(0.4)
    ui.step = total
    measurements.markers_found = len(results["ids"])
    time.sleep(2)
