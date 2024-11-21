import numpy as np
import matplotlib.pyplot as plt
import time


# Generating a set of 200 Points with random X and Y coordinates and extracting coordinates into seperate arrays
points = np.random.randint(0, 10001, size=(200, 2))
x_coords, y_coords = points[:,0], points[:,1]

# Start timing
start_time = time.time()

# QuickHull Algorithm -> Barber et al. (1966) https://dpd.cs.princeton.edu/Papers/BarberDobkinHuhdanpaa.pdf
def QuickHull(points):
    """
    Do the QuickHull Algorithm
    """
    def find_side(p1, p2, p):
        """
        Determines if the point p is left or right to the line p1...p2
        """
        return (p[1] - p1[1]) * (p2[0] - p1[0]) - (p[0] - p1[0]) * (p2[1] - p1[1])

    def hull_subset(p1, p2, subset_points):
        """
        Finds hull points on one side of the line p1...p2
        """
        if not subset_points:
            return []
        # Find the farthest point from the line (p1, p2)
        farthest = max(subset_points, key=lambda p: abs(find_side(p1, p2, p)))
        # Divide points into subsets based on which side of the lines they lie
        left_of_line = [p for p in subset_points if find_side(p1, farthest, p) > 0]
        right_of_line = [p for p in subset_points if find_side(farthest, p2, p) > 0]

        # Recurse to find the hull points
        return hull_subset(p1, farthest, left_of_line) + [farthest] + hull_subset(farthest, p2, right_of_line)

    # Find the leftmost and rightmost points
    min_point = min(points, key=lambda p: p[0])
    max_point = max(points, key=lambda p: p[0])

    # Divide points into subsets on either side of the line (min_point, max_point)
    left_set = [p for p in points if find_side(min_point, max_point, p) > 0]
    right_set = [p for p in points if find_side(max_point, min_point, p) > 0]

    # Construct the hull via recursion
    hull = [min_point] + hull_subset(min_point, max_point, left_set) + \
           [max_point] + hull_subset(max_point, min_point, right_set)
    return hull

# Run the QuickHull algorithm and extract the coordinates of the hull points
convex_hull = QuickHull(points)
hull_x, hull_y = zip(*convex_hull)


# Stop timing
end_time = time.time()
computation_time_ms = (end_time - start_time)*1000


# Print Point List with coordinates
print("Point List (Point Number, X-Coordinate, Y-Coordinate):")
for i, (x, y) in enumerate(points):
    print(f"Point {i+1}: ({x}, {y})")

# Print Convex Hull Point Numbers
hull_indices = []
for hull_point in convex_hull:
    index = np.where(np.all(points == hull_point, axis=1))[0][0]
    hull_indices.append(index + 1)  # indices starting from 1
hull_indices.sort()
print("\nConvex Hull (Point Numbers):")
print(hull_indices)


# Create figure with points and Convex Hull
plt.figure(figsize=(8, 8))
plt.scatter(x_coords, y_coords, color='blue', marker='o', s=10, label="Points")
plt.plot(hull_x + (hull_x[0],), hull_y + (hull_y[0],), color='red', lw=2, label="Convex Hull")
plt.title("Convex Hull using QuickHull")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(title=f"Computation Time: {computation_time_ms:.2f} ms\nPoints on Hull: {len(convex_hull)}")
plt.show()
