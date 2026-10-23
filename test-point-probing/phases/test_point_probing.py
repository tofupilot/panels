"""Probes the board's 19 bottom-side test points with the bed-of-nails
fixture. `ui.tp1` to `ui.tp19` turn each one green or red against its
expected level, `ui.px` and `ui.py` move the probe over the KiCad drawing
(0.1 mm units, bottom side mirrored), `ui.tag` names the net and the reading.
The run records USB0_VBUS and the USB1_FAULT pull-up."""
import time

BOARD_WIDTH = 716
TEST_POINTS = [[1, "DBGEN", 565, 349], [2, "TRST", 537, 364], [3, "LED1", 590, 121], [4, "LED2", 648, 213], [5, "LED3", 538, 429], [6, "LED4", 626, 432], [7, "USB1_VBUS", 94, 259], [8, "USB1_SENSE", 129, 231], [9, "SPIFI_CS", 182, 141], [10, "USB1_EN", 200, 226], [11, "USB1_FAULT", 127, 193], [12, "USB1_ID", 102, 315], [13, "USB0_ID", 536, 297], [14, "USB0_VBUS", 626, 309], [15, "USB0_SENSE", 573, 307], [16, "TMS", 597, 409], [17, "TCK", 597, 383], [18, "TDO", 495, 369], [19, "TDI", 430, 349]]
EXPECTED = {"DBGEN": (0, 0.3), "USB1_VBUS": (0, 0.3), "USB1_SENSE": (0, 0.3), "USB1_EN": (0, 0.3), "TCK": (0, 0.3),
            "USB0_VBUS": (4.75, 5.25), "USB0_SENSE": (1.5, 1.8)}


def probe(ui, measurements, fixture):
    for number, net, x, y in TEST_POINTS:
        ui.px, ui.py = x, y
        ui.side = "l" if x > BOARD_WIDTH - 360 else "r"
        time.sleep(0.3)
        volts = fixture.probe(net)
        low, high = EXPECTED.get(net, (3.0, 3.6))
        ok = low <= volts <= high
        ui.tag = f"TP{number} {net} {volts:.2f} V"
        setattr(ui, f"tp{number}", "pass" if ok else "fail")
        if net == "USB0_VBUS":
            measurements.usb0_vbus = volts
        if net == "USB1_FAULT":
            measurements.usb1_fault = volts
        time.sleep(0.6 if ok else 1.4)
    time.sleep(1.5)
