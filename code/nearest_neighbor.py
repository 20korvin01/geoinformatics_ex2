import numpy as np
import matplotlib.pyplot as plt


# Generate a set of 200 2D points with random X and Y coordinates in [0, 10000]
pointsA = np.random.randint(0, 10000, (200, 2))
pointsB = np.random.randint(0, 10000, (20, 2))

### Task find the nearest neighbor for each point in A to B
def nearest_neighbor(src, dst):
     dist = np.linalg.norm(src[:, None] - dst, axis=-1)
     indices = dist.argmin(-1)
     return dist[np.arange(len(dist)), indices], indices

distance, neighbor_index =  nearest_neighbor(pointsA, pointsB)

plt.scatter(pointsA[:, 0], pointsA[:, 1])
plt.scatter(pointsB[:,0], pointsB[:,1], color="r")

## Drawing for every nearest point a line to point A
def line_to_nearest_point(pointsA, nearest_points_index, pointsB):
    for points_coordinates, neighbor_index in zip(pointsA, nearest_points_index):
        pointA = [points_coordinates[0],pointsB[neighbor_index][0]]
        pointB = [points_coordinates[1],pointsB[neighbor_index][1]]
        plt.plot(pointA, pointB, color="k")         

line_to_nearest_point(pointsA, neighbor_index, pointsB)

plt.show()
