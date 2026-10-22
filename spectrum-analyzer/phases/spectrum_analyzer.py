"""Watches the S-band downlink on the spectrum analyzer while the
transmitter comes up. `ui.s0` to `ui.s47` are the trace in dBm, `ui.pk` and
`ui.pl` place the marker on the peak, `ui.mkr` is its readout. The run records
the carrier's peak level."""
import time

CENTER_MHZ, SPAN_MHZ = 2245.0, 2.0


def acquire(ui, measurements, analyzer):
    peak = -200.0
    for n in range(analyzer.length()):
        trace = analyzer.sweep()
        if n % 3 == 0:
            for k, dbm in enumerate(trace):
                setattr(ui, f"s{k}", round(dbm, 1))
            bin_ = max(range(len(trace)), key=trace.__getitem__)
            peak = trace[bin_]
            mhz = CENTER_MHZ + (bin_ / (len(trace) - 1) - 0.5) * SPAN_MHZ
            ui.pk = bin_
            ui.pl = round(peak, 1)
            ui.mkr = f"MKR1 {mhz / 1000:.6f} GHz {peak:.1f} dBm"
        time.sleep(0.1)
    measurements.carrier_level = round(peak, 1)
    time.sleep(1.5)
