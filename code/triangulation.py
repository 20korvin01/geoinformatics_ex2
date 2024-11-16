## EXERCISE I
#TODO Triangulation

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

#? Input:
# A set of 200 2D-Points with random X and Y coordinates within the interval [0, 10000].
points = np.random.randint(0, 10000, (200, 2))

#? Algorithm:
# Implementation of a triangulation on the generated point set.
tri = Delaunay(points)

#? Plot
# Plot the triangulation with the generated points.
plt.triplot(points[:,0], points[:,1], tri.simplices)
plt.plot(points[:,0], points[:,1], 'o')
plt.show()

#? Output:
# Point List (Point Number, X-Coordinate, Y-Coordinate).
# Triangulation (Triangle Number, Point Number 1, Point Number 2, Point Number 3).
points = np.concatenate((np.arange(points.shape[0])[:, None], points), axis=1)
triangles = np.concatenate((np.arange(tri.simplices.shape[0])[:, None], tri.simplices), axis=1)

print("Point List:")
print(points)
print("\nTriangulation:")
print(triangles)

