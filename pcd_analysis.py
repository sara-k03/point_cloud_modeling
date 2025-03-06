import numpy as np 
import open3d as o3d
import plotly.graph_objects as go

# reads point cloud from pcd
# change the file name for where your data is located
pcd = o3d.io.read_point_cloud("Datasets/PCD_1.pcd")
#stores point clouds in array
output = np.asarray(pcd.points)  

# 3D Scatter Plot
fig = go.Figure( data = [ go.Scatter3d (
    x = output[:, 0],  # X-coordinates
    y = output[:, 1],  # Y-coordinates
    z = output[:, 2],  # Z-coordinates
    mode = 'markers',
    marker = dict(size=2, color=output[:, 2], colorscale='Viridis', opacity=0.8)
)])

# Labels & rotation
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ),
    title="Interactive 3D Point Cloud",
)

fig.show()
