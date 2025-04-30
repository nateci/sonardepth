import pandas as pd
import plotly.graph_objects as go

def plot_3d_bathymetry(df: pd.DataFrame):
    """
    Render a 3D surface plot of the bathymetric data using Plotly.
    """
    pivot = df.pivot_table(values='depth', index='y', columns='x')
    x = pivot.columns
    y = pivot.index
    z = pivot.values

    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Viridis')])
    fig.update_layout(
        title='3D Bathymetric Map',
        scene=dict(
            xaxis_title='X Position (m)',
            yaxis_title='Y Position (m)',
            zaxis_title='Depth (m)',
            zaxis=dict(autorange='reversed')
        ),
        autosize=True,
        margin=dict(l=0, r=0, t=50, b=0)
    )
    fig.show()
