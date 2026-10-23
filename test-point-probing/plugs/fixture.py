"""Mock bed-of-nails fixture: the voltage on each of the GreatFET One's 19
bottom-side test points with the board powered. Replace it with your
fixture's driver."""

READINGS = {
    "DBGEN": 0.00, "TRST": 3.30, "LED1": 3.30, "LED2": 3.30, "LED3": 3.30, "LED4": 3.30, "USB1_VBUS": 0.00,
    "USB1_SENSE": 0.01, "SPIFI_CS": 3.30, "USB1_EN": 0.00, "USB1_FAULT": 3.29, "USB1_ID": 3.29, "USB0_ID": 3.29,
    "USB0_VBUS": 5.02, "USB0_SENSE": 1.66, "TMS": 3.30, "TCK": 0.00, "TDO": 3.30, "TDI": 3.30,
}


class Fixture:
    def probe(self, net):
        """Volts on the test point of a net."""
        return READINGS[net]
