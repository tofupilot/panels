"""Mock station camera: the ChArUco detections and the calibration OpenCV computed on the rig photo. Replace it with your camera and the OpenCV calls of your station."""
import json

RESULTS = json.loads("{\"targets\":[[35,54],[35,54],[35,54],[35,54]],\"rms\":0.24,\"fx\":2977.8,\"target_rms\":[0.263,0.232,0.222,0.243]}")


class RigCamera:
    def results(self):
        return RESULTS
