import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt


# generate 200 random 2D points between 0 and 10000 in the from: (i, x, y)
points = np.random.randint(0, 10000, (200, 2))

# plot the points
plt.scatter(points[:, 0], points[:, 1], s=1)
plt.show()