"""Mock RF checkout equipment: replays a downlink acquisition, the carrier,
then bit sync, then frame sync, while Eb/N0 rises as the antenna coupler is
set, one reading per call. Replace it with your RF SCOE's driver on a real
bench."""
import math


class RfScoe:
    def __init__(self):
        self.k = 0

    def length(self):
        return 170

    def read(self):
        """[carrier lock, bit sync, frame sync, Eb/N0 in dB, good frames]"""
        k = self.k
        self.k += 1
        ebn0 = max(0.0, 12.4 * (1 - math.exp(-k / 35)) + 0.25 * math.sin(k * 1.7))
        carrier, bit_sync, frame_sync = k > 18, k > 34, k > 52
        frames = max(0, (k - 52) * 8) if frame_sync else 0
        return [carrier, bit_sync, frame_sync, round(ebn0, 2), frames]
