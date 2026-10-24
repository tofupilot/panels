"""Mock calibration results: each rig target's pose relative to the camera, from the OpenCV calibration. Replace it with your camera and the OpenCV calls of your station."""
import json

RESULTS = json.loads("{\"tilts\":[29.5,30.0,29.9,28.1],\"distances\":[1.217,1.194,1.219,1.227]}")


class PoseResults:
    def results(self):
        return RESULTS
