import numpy as np

SPEED_OF_SOUND_WATER = 1500  # meters per second

def simulate_echo_time(depth: float, noise: float = 0.001) -> float:
    """
    Simulates the round-trip time for a sonar echo given a depth (in meters).
    Adds a small amount of random noise.
    """
    true_time = 2 * depth / SPEED_OF_SOUND_WATER
    return true_time + np.random.normal(0, noise)
