"""Routes the multimeter through the switch matrix to each test node in turn:
ABUS1 on the node, ABUS2 on ground. `ui.x{bus}_{column}` lights the closed
crosspoints. The run records VREF and the 3V3 node."""
import time

GND = 15
RECORD = {3: "v3v3", 6: "vref"}


def scan_nodes(ui, measurements, switch_matrix):
    for node in range(15):
        switch_matrix.close(0, node)
        switch_matrix.close(1, GND)
        setattr(ui, f"x0_{node}", True)
        setattr(ui, f"x1_{GND}", True)
        for _ in range(8):
            volts = switch_matrix.read_dc()
            time.sleep(0.1)
        if node in RECORD:
            setattr(measurements, RECORD[node], round(volts, 4))
        switch_matrix.open_all()
        setattr(ui, f"x0_{node}", False)
        setattr(ui, f"x1_{GND}", False)
        time.sleep(0.1)
    time.sleep(1.5)
