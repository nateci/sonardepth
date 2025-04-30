import os
from src.generate_data import generate_vessel_sweep_data
from src.plot_error import plot_depth_error

def main():
    os.makedirs("data", exist_ok=True)
    df = generate_vessel_sweep_data()
    df.to_csv("data/vessel_sweep.csv", index=False)
    print("Saved simulated vessel sweep to data/vessel_sweep.csv")
    plot_depth_error(df)

if __name__ == "__main__":
    main()
