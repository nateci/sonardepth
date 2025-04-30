import numpy as np
import pandas as pd
from src.sonar_math import simulate_echo_time, SPEED_OF_SOUND_WATER

def generate_vessel_sweep_data(x_start=0, x_end=100, y_fixed=50, step=1):
    """
    Simulate sonar pings along a straight vessel path.
    """
    data = []

    for x in range(x_start, x_end + 1, step):
        # True depth based on location
        true_depth = 50 + 10 * np.sin(x / 10) * np.cos(y_fixed / 10)

        # Simulate sonar echo + measurement
        echo_time = simulate_echo_time(true_depth)
        measured_depth = SPEED_OF_SOUND_WATER * echo_time / 2

        # Compute error
        error = measured_depth - true_depth

        data.append((x, y_fixed, true_depth, measured_depth, error))

    return pd.DataFrame(data, columns=["x", "y", "true_depth", "measured_depth", "error"])
