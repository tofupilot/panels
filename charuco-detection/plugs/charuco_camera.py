"""Mock station camera: the ChArUco markers, corners and board pose OpenCV found on the rotary-stage photo. Replace it with your camera and the OpenCV calls of your station."""
import json

RESULTS = json.loads("{\"markers\":17,\"corners\":24}")


class CharucoCamera:
    def results(self):
        return RESULTS
