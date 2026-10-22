"""Acquires the downlink on the RF checkout equipment. The panel lights
`ui.carrier`, `ui.bit_sync` and `ui.frame_sync`, fills its tape with
`ui.ebn0`, and turns amber with `ui.link_state` below 9.6 dB once locked, the
Eb/N0 uncoded BPSK needs for a bit error rate of 1e-5. The run records the
mean Eb/N0 with frame sync."""
import time

THRESHOLD_DB = 9.6


def acquire_downlink(ui, measurements, scoe):
    locked = []
    for _ in range(scoe.length()):
        carrier, bit_sync, frame_sync, ebn0, frames = scoe.read()
        ui.carrier = carrier
        ui.bit_sync = bit_sync
        ui.frame_sync = frame_sync
        ui.ebn0 = ebn0
        ui.frames = f"{frames} FRAMES" if frame_sync else "SEARCHING"
        ui.link_state = "warn" if frame_sync and ebn0 < THRESHOLD_DB else "ok"
        if frame_sync:
            locked.append(ebn0)
        time.sleep(0.1)
    measurements.eb_n0 = round(sum(locked[-60:]) / len(locked[-60:]), 2)
    time.sleep(1.5)
