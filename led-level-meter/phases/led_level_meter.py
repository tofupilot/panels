"""Steps a 1 kHz tone up to the +4 dBu nominal level and reads both outputs.
`ui.l` and `ui.r` light the bargraphs in dBu, `ui.lp` and `ui.rp` hold each
peak for two seconds. The run records both levels at nominal."""
import time

HOLD_S = 2.0


def level(ui, measurements, audio_analyzer):
    peaks = {"l": (-99.0, 0.0), "r": (-99.0, 0.0)}
    t, last = 0.0, (0.0, 0.0)
    for _ in range(audio_analyzer.length()):
        left, right = audio_analyzer.read()
        for ch, db in (("l", left), ("r", right)):
            setattr(ui, ch, round(db, 2))
            held, since = peaks[ch]
            if db > held or t - since > HOLD_S:
                peaks[ch] = (db, t)
            setattr(ui, f"{ch}p", round(peaks[ch][0], 2))
        last = (left, right)
        t += 0.1
        time.sleep(0.1)
    measurements.level_left = round(last[0], 2)
    measurements.level_right = round(last[1], 2)
    time.sleep(1.5)
