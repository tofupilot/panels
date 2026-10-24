"""Mock logic analyzer on the I2C bus of a TMP117 temperature sensor at
0x48: a pointer write to register 0x00, a repeated start, then the two
temperature bytes. Replace it with your analyzer's driver."""


class LogicAnalyzer:
    def capture(self):
        """The decoded read: address, register and the two data bytes."""
        return {"address": 0x48, "register": 0x00, "data": [0x0C, 0x80]}
