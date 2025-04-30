import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

def plot_3d_true_depth_colored_by_error(df: pd.DataFrame, output_path="data/depth_error_colormap.html"):
    """
    Plot the true seafloor surface but color it based on measurement error.
    """
    pivot_depth = df.pivot_table(values='true_depth', index='y', columns='x')
    pivot_error = df.pivot_table(values='error', index='y', columns='x')

    x = pivot_depth.columns
    y = pivot_depth.index
    z = pivot_depth.values
    color_error = pivot_error.values

    fig = go.Figure(data=[
        go.Surface(
            z=z,
            x=x,
            y=y,
            surfacecolor=color_error,
            colorscale='RdBu',
            colorbar=dict(title="Error (m)"),
            cmin=-abs(color_error).max(),
            cmax=abs(color_error).max()
        )
    ])

    fig.update_layout(
        title='True Bathymetry Colored by Sonar Error',
        scene=dict(
            xaxis_title='X (m)',
            yaxis_title='Y (m)',
            zaxis_title='True Depth (m)',
            zaxis=dict(autorange='reversed')
        ),
        margin=dict(l=0, r=0, t=50, b=0)
    )

    pio.write_html(fig, file=output_path, auto_open=True)
    print(f"Saved colored error surface plot to: {output_path}")
