"""Mock DC supply current into the product as its stages switch on: standby,
the main board, the motor drive, then the steady load. Replace it with your
shunt or current meter's driver."""

STAGES = [0.0, 0.82, 0.82, 2.35, 2.35, 3.1, 3.1, 2.84, 2.84, 2.84, 0.0, 0.0]


class LoadAmmeter:
    def __init__(self):
        self.k = 0

    def length(self):
        return len(STAGES) * 13

    def read(self):
        """[stage index, amps]"""
        stage = min(self.k // 13, len(STAGES) - 1)
        self.k += 1
        return [stage, STAGES[stage]]
