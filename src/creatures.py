import numpy as np

def get_creature_interference(x, y):
    """
    Simulate sonar distortion caused by underwater creatures or plants.
    Returns a depth offset (positive or negative) based on presence.
    """

    # Example fish locations (x, y): subtract depth to simulate early echo
    fish_zones = [((30, 50), 5), ((60, 30), 3)]
    
    # Example seaweed bed: add noisy depth to simulate noisy returns
    weed_zone = (40, 40, 15)  # center_x, center_y, radius
    max_noise = 8
    
    interference = 0

    # Fish interference (early return, shallower depth)
    for (cx, cy), intensity in fish_zones:
        if abs(x - cx) < 3 and abs(y - cy) < 3:
            interference -= intensity

    # Seaweed interference (later return, deeper depth + noise)
    wx, wy, radius = weed_zone
    distance = np.sqrt((x - wx)**2 + (y - wy)**2)
    if distance < radius:
        interference += np.random.normal(loc=2, scale=1)

    return interference
