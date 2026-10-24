"""Finds the chessboard's inner corners. `ui.found` reveals them row by
row as OpenCV orders them. The run records how many corners it found."""
import time


def find_corners(ui, measurements, chessboard_camera):
    results = chessboard_camera.results()
    for _ in range(3):
        for found in range(0, results["corners"] + 1, 2):
            ui.found = found
            time.sleep(0.1)
        time.sleep(1.5)
        ui.found = -1
        time.sleep(0.4)
    ui.found = results["corners"]
    measurements.corners_found = results["corners"]
    time.sleep(2)
