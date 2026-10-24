"""Detects the ChArUco board: `ui.step` reveals its markers, then its
corners, then the board's pose axes. The run records the markers and corners
found."""
import time


def detect_board(ui, measurements, charuco_camera):
    results = charuco_camera.results()
    total = results["markers"] + results["corners"] + 3
    for _ in range(3):
        for step in range(total + 1):
            ui.step = step
            time.sleep(0.12)
        time.sleep(1.5)
        ui.step = -1
        time.sleep(0.4)
    ui.step = total
    measurements.markers_found = results["markers"]
    measurements.corners_found = results["corners"]
    time.sleep(2)
