"""Steps the multimeter's scanner through the board's four rails. `ui.v*`
drive the seven glyphs of the 6 1/2-digit reading, `ui.chn`, `ui.lim` and
`ui.res` the channel, the limit and the verdict. The run records each rail."""
import time


def show(ui, prefix, text):
    """One 7-segment glyph per character, decimal points left to the panel."""
    for k, ch in enumerate(c for c in text if c != "."):
        setattr(ui, f"{prefix}{k}", "_" if ch == " " else ch)

RAILS = [(101, "VBUS", "vbus", 5.0), (102, "3V3", "v3v3", 3.3), (103, "USB1_VBUS", "usb1_vbus", 5.0), (104, "VBAT", "vbat", 3.3)]


def rails(ui, measurements, multimeter):
    for channel, name, key, nominal in RAILS:
        low, high = nominal * 0.97, nominal * 1.03
        ui.chn = f"CH {channel}  {name}"
        ui.lim = f"LIMIT {low:.3f} … {high:.3f} V"
        for _ in range(40):
            volts = multimeter.read_dc(channel)
            show(ui, "v", f"{volts:08.5f}")
            ui.res = "PASS" if low <= volts <= high else "FAIL"
            time.sleep(0.1)
        setattr(measurements, key, round(volts, 5))
    time.sleep(1.5)
