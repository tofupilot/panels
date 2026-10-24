"""Reads the calibration's reprojection error back: `ui.e1` to `ui.e4` are
each target's RMS in pixels, `ui.shown` reveals the corner residuals target by
target. The run records the overall RMS and the worst target's."""
import time


def check_calibration(ui, measurements, calibration_results):
    results = calibration_results.results()
    for _ in range(2):
        for index, rms in enumerate(results["target_rms"], 1):
            setattr(ui, f"e{index}", rms)
            ui.shown = index - 1
            time.sleep(0.9)
        time.sleep(2.5)
        for index in range(1, 5):
            setattr(ui, f"e{index}", 0)
        ui.shown = -1
        time.sleep(0.8)
    for index, rms in enumerate(results["target_rms"], 1):
        setattr(ui, f"e{index}", rms)
    ui.shown = 3
    measurements.reprojection_rms = results["rms"]
    measurements.worst_target_rms = max(results["target_rms"])
    time.sleep(2)
