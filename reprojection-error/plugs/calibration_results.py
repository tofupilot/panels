"""Mock calibration results: each rig target's reprojection error from the OpenCV calibration. Replace it with your camera and the OpenCV calls of your station."""
import json

RESULTS = json.loads("{\"target_rms\":[0.263,0.232,0.222,0.243],\"rms\":0.24}")


class CalibrationResults:
    def results(self):
        return RESULTS
