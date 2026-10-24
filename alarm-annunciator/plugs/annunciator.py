"""Mock station alarm annunciator through one incident: the air supply drops,
LOW AIR comes in first, VAC LOSS follows, the operator acknowledges, the air
returns and both clear. Replace it with your PLC or alarm system's driver."""

# [from, to] in seconds, per alarm: first-out flash, then steady once acknowledged.
TIMELINE = {
    "hv_on": [(0.6, 2.6, "on")],
    "low_air": [(3.6, 5.0, "first"), (5.0, 7.7, "on")],
    "vac_loss": [(4.1, 5.0, "new"), (5.0, 7.4, "on")],
    "dut_power": [(0.0, 99, "on")],
}


class Annunciator:
    def states(self, t):
        """{alarm: "" | "first" | "new" | "on"} at t seconds into the incident."""
        out = {}
        for name, spans in TIMELINE.items():
            out[name] = next((s for a, b, s in spans if a <= t < b), "")
        return out
