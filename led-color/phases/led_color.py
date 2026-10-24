"""Reads the board's eight LEDs with the LED analyzer, one fiber at a time.
`ui.cx` and `ui.cy` move the ring to where the LED's chromaticity falls on
the drawn CIE 1931 diagram, `ui.d1` to `ui.d8` drop each point into place.
The run records the red D1's x and the white D8's y."""
import time

# The diagram's scale in panel units: x 0..0.75 over 274.0 px from 34, y 0..0.85 over 176 px up from 192.
X0, SX, Y0, SY = 34, 365.3333, 192, 207.0588


def measure_leds(ui, measurements, led_analyzer):
    for index in range(8):
        x, y, mcd = led_analyzer.measure(index)
        ui.cx, ui.cy = round(X0 + x * SX, 1), round(Y0 - y * SY, 1)
        time.sleep(0.4)
        setattr(ui, f"d{index + 1}", "measured")
        if index == 0:
            measurements.red_x = x
        if index == 7:
            measurements.white_y = y
        time.sleep(1.2)
    time.sleep(1.5)
