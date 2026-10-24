"""Demodulates the carrier while the amplifier is tuned. `ui.qi*` and `ui.qq*`
are a pool of 160 received symbols, the oldest 16 replaced every update. The
run records the EVM and the MER of the last symbols, from the noise sigma."""
import math
import time

POOL, BATCH = 160, 16


def modulation_quality(ui, measurements, signal_analyzer):
    sigma = 1.0
    for n in range(signal_analyzer.length()):
        symbols, sigma = signal_analyzer.symbols(BATCH)
        base = (n * BATCH) % POOL
        for k, (i, q) in enumerate(symbols):
            setattr(ui, f"qi{base + k}", round(i, 3))
            setattr(ui, f"qq{base + k}", round(q, 3))
        time.sleep(0.1)
    # 16-QAM on the -3..3 grid: average symbol power 10, noise power 2 sigma^2.
    evm = math.sqrt(2 * sigma ** 2 / 10)
    measurements.evm = round(100 * evm, 2)
    measurements.mer = round(-20 * math.log10(evm), 1)
    time.sleep(1.5)
