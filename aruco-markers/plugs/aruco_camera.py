"""Mock station camera: the six ArUco markers and their poses OpenCV found on the fixture-plate photo. Replace it with your camera and the OpenCV calls of your station."""
import json

RESULTS = json.loads("{\"ids\":[3,41,12,26,19,7]}")


class ArucoCamera:
    def results(self):
        return RESULTS
