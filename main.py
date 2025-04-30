from src.generate_data import generate_bathymetry_grid
from src.plot_surface import plot_3d_surface
import os
from src.plot_error import plot_3d_true_depth_colored_by_error

def main():
    os.makedirs("data", exist_ok=True)
    df = generate_bathymetry_grid()
    df.to_csv("data/grid_sweep.csv", index=False)

    plot_3d_surface(df)
    plot_3d_true_depth_colored_by_error(df)


if __name__ == "__main__":
    main()
