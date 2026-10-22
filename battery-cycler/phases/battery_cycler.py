"""Charges and discharges the pack on the cycler. The panel shows the
channel's front: `ui.v*` and `ui.i*` drive its 7-segment digits, `ui.cc`,
`ui.cv`, `ui.chg`, `ui.dsg` and `ui.ocp` its annunciators. The run records
the constant-current charge current and the voltage held in CV."""
import time


def show(ui, prefix, text):
    """One 7-segment glyph per character, decimal points left to the panel."""
    for k, ch in enumerate(c for c in text if c != "."):
        setattr(ui, f"{prefix}{k}", "_" if ch == " " else ch)


def charge_and_discharge(ui, measurements, cycler):
    cc, cv = [], []
    for _ in range(cycler.length()):
        s = cycler.read()
        volts, amps = s["voltage"], s["current"]
        show(ui, "v", f"{volts:5.2f}")
        show(ui, "i", ("-" if amps < -0.05 else " ") + f"{min(abs(amps), 99.9):4.1f}")
        ui.cc = s["step"] in ("CC", "DSG")
        ui.cv = s["step"] == "CV"
        ui.chg = amps > 0.05
        ui.dsg = amps < -0.05
        ui.ocp = amps < -85 or amps > 60
        ui.out = abs(amps) > 0.05
        if s["step"] == "CC":
            cc.append(amps)
        if s["step"] == "CV":
            cv.append(volts)
        time.sleep(0.1)
    measurements.cc_charge_current = round(sum(cc) / len(cc), 2)
    measurements.cv_voltage = round(sum(cv) / len(cv), 2)
    time.sleep(1.5)
