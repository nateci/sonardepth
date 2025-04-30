import numpy as np
import pandas as pd
from src.sonar_math import simulate_echo_time, SPEED_OF_SOUND_WATER
from creatures import get_creature_interference

def generate_bathymetry_grid(x_range=(0, 100), y_range=(0, 100), resolution=5):
    x_vals = np.arange(x_range[0], x_range[1] + 1, resolution)
    y_vals = np.arange(y_range[0], y_range[1] + 1, resolution)
    data = []

    for x in x_vals:
        for y in y_vals:
            true_depth = 50 + 10 * np.sin(x / 10) * np.cos(y / 10)
            interference = get_creature_interference(x, y)
            echo_time = simulate_echo_time(true_depth + interference)
            echo_time = simulate_echo_time(true_depth)
            measured_depth = SPEED_OF_SOUND_WATER * echo_time / 2
            error = measured_depth - true_depth
            data.append((x, y, true_depth, measured_depth, error))
            

    return pd.DataFrame(data, columns=["x", "y", "true_depth", "measured_depth", "error"])

