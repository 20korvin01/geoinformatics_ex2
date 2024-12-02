import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
import scipy as sc
# Generate a set of 200 2D points with random X and Y coordinates in [0, 10000]
pointsA = np.random.randint(0, 10000, (200, 2))
pointsB = np.random.randint(0, 10000, (20, 2))

### Task find the nearest neighbor for each point in A to B
#def nearest_neighbor(src, dst):
#     dist = np.linalg.norm(src[:, None] - dst, axis=-1)
#     indices = dist.argmin(-1)
#     return dist[np.arange(len(dist)), indices], indices
#

def nearest_neighbors_kd_tree(x, y, k) :
    x, y = map(np.asarray, (x, y))
    tree =sc.spatial.cKDTree(y[:, None])    
    ordered_neighbors = tree.query(x[:, None], k)[1]
    nearest_neighbor = np.empty((len(x),), dtype=np.intp)
    nearest_neighbor.fill(-1)
    used_y = set()
    for j, neigh_j in enumerate(ordered_neighbors) :
        for k in neigh_j :
            if k not in used_y :
                nearest_neighbor[j] = k
                used_y.add(k)
                break
    return nearest_neighbor

print(pointsB)

#distance, neighbor_index =  nearest_neighbor(pointsA, pointsB)
nearest_neighbors = nearest_neighbors_kd_tree(pointsA, pointsB, 1)

plt.scatter(pointsA[:, 0], pointsA[:, 1])
plt.scatter(pointsB[:,0], pointsB[:,1], color="r")

## Drawing for every nearest point a line to point A
#def line_to_nearest_point(pointsA, nearest_points_index, pointsB):
#    for points_coordinates, neighbor_index in zip(pointsA, nearest_points_index):
#        pointA = [points_coordinates[0],pointsB[neighbor_index][0]]
#        pointB = [points_coordinates[1],pointsB[neighbor_index][1]]
#        plt.plot(pointA, pointB, color="k")         

def line_to_nearest_point(pointsA, nearest_neighbors):
    for points_coordinates, neighbor_coordinates in zip(pointsA, nearest_neighbors):
        pointA = [points_coordinates[0], neighbor_coordinates[0]]
        pointB = [points_coordinates[1], neighbor_coordinates[1]]
        plt.plot(pointA, pointB, color="k")         

line_to_nearest_point(pointsA, nearest_neighbors)

plt.show()
