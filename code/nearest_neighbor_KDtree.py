import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as sc

# Generate a set of 200 2D points with random X and Y coordinates in [0, 10000]
pointsA = np.random.randint(0, 10000, (200, 2))
pointsB = np.random.randint(0, 10000, (20, 2))

# Function to find nearest neighbors using KDTree
def nearest_neighbors_kd_tree(x, y, k):
    x, y = map(np.asarray, (x, y))
    tree = sc.cKDTree(y)
    index, ordered_neighbors = tree.query(x, k)  
    nearest_neighbors = y[ordered_neighbors]  # Retrieve the coordinates of the nearest neighbors
    return nearest_neighbors

# Find single nearest neighbors for each point in pointsA from pointsB
nearest_neighbors = nearest_neighbors_kd_tree(pointsA, pointsB, 1)

# Plot the points
plt.scatter(pointsA[:, 0], pointsA[:, 1], label="Points A")
plt.scatter(pointsB[:, 0], pointsB[:, 1], color="r", label="Points B")

# Draw neighbors with connected lines 
def line_to_nearest_point(pointsA, nearest_neighbors):
    for pointA, neighbor in zip(pointsA, nearest_neighbors):
        plt.plot([pointA[0], neighbor[0]], [pointA[1], neighbor[1]], color="k")

line_to_nearest_point(pointsA, nearest_neighbors)
plt.legend()
plt.show()

