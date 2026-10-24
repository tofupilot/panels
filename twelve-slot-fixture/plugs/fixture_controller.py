"""Mock 12-slot fixture: each slot starts 0.6 s after the previous one and
runs its board through flash, rails, USB and LEDs in 6 s. Slot 7 fails once
on USB and passes its retest. Replace it with your fixture's controller."""

SLOTS = 12
START, RUN = 0.6, 6.0


class FixtureController:
    def state(self, t):
        """Per slot: (state, progress 0..1), state in wait, run, retest, pass."""
        out = []
        for s in range(SLOTS):
            u = (t - s * START) / RUN
            if s == 6:
                if 0 <= u < 0.7:
                    out.append(("run", u))
                    continue
                if 0.7 <= u < 0.95:
                    out.append(("retest", 0.7))
                    continue
                u = (t - s * START - 0.95 * RUN) / RUN
            if u < 0:
                out.append(("wait", 0.0))
            elif u < 1:
                out.append(("run", u))
            else:
                out.append(("pass", 1.0))
        return out
