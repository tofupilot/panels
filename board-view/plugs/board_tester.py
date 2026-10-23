"""Mock functional tester walking the GreatFET One's top side: the 3.3 V
regulator, USB0, the MCU, the SPI flash, the USB1 power switch, the LEDs and
the buttons. Replace it with your own checks."""

RESULTS = {
    "regulator": (True, "3.299 V", 3.299),
    "usb0": (True, "1d50:60e6", None),
    "mcu": (True, "LPC4330", None),
    "flash": (True, "EF 40 15", None),
    "usb1": (True, "port off, no fault", None),
    "leds": (True, "4 / 4 lit", None),
    "buttons": (True, "DFU, RESET", None),
}


class BoardTester:
    def check(self, name):
        """[passed, readout, value or None]"""
        return list(RESULTS[name])
