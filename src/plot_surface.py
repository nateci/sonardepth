import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

def plot_3d_surface(df: pd.DataFrame, output_path="data/bathymetry_plot.html"):
    pivot = df.pivot_table(values='measured_depth', index='y', columns='x')
    x = pivot.columns
    y = pivot.index
    z = pivot.values

    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Viridis')])
    fig.update_layout(
        title='Simulated Bathymetric Surface (Measured Depth)',
        scene=dict(
            xaxis_title='X (meters)',
            yaxis_title='Y (meters)',
            zaxis_title='Depth (meters)',
            zaxis=dict(autorange='reversed')
        ),
        margin=dict(l=0, r=0, t=50, b=0)
    )

    # Save to HTML
    pio.write_html(fig, file=output_path, auto_open=True)
    print(f"Saved interactive 3D plot to: {output_path}")
