import pandas as pd
import matplotlib.pyplot as plt

def plot_depth_error(df: pd.DataFrame):
    plt.figure(figsize=(10, 4))
    plt.plot(df['x'], df['true_depth'], label='True Depth', color='blue')
    plt.plot(df['x'], df['measured_depth'], label='Measured Depth', color='orange', linestyle='--')
    plt.fill_between(df['x'], df['true_depth'], df['measured_depth'], color='gray', alpha=0.3)
    plt.title("Simulated Sonar Depth Measurement vs. True Depth")
    plt.xlabel("X Position (m)")
    plt.ylabel("Depth (m)")
    plt.gca().invert_yaxis()
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
