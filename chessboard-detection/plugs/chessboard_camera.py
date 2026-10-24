"""Mock station camera: the chessboard corners OpenCV found on the tilt-stage photo. Replace it with your camera and the OpenCV calls of your station."""
import json

RESULTS = json.loads("{\"corners\":54,\"pattern\":[9,6]}")


class ChessboardCamera:
    def results(self):
        return RESULTS
