"""Watches the board heat up in burn-in through the thermal camera. `ui.h0`
to `ui.h107` are the camera's 12 x 9 grid in C, drawn over the KiCad layout;
`ui.hx` and `ui.hy` place the hot spot marker (0.1 mm units) and `ui.tmax`
is its reading. The run records the hottest point against the 85 C limit."""
import time

COLS, WIDTH, HEIGHT = 12, 716, 543


def burn_in(ui, measurements, thermal_camera):
    shown = {}
    hottest = 0.0
    for _ in range(thermal_camera.length()):
        grid = thermal_camera.frame()
        for k, temp in enumerate(grid):
            value = round(temp * 2) / 2
            if shown.get(k) != value:
                setattr(ui, f"h{k}", value)
                shown[k] = value
        k = max(range(len(grid)), key=grid.__getitem__)
        hottest = grid[k]
        ui.hx = round((k % COLS + 0.5) * WIDTH / COLS)
        ui.hy = round((k // COLS + 0.5) * HEIGHT / (len(grid) // COLS))
        ui.tmax = f"{hottest:.1f} °C"
        time.sleep(0.5)
    measurements.max_temperature = round(hottest, 1)
    time.sleep(1.5)
