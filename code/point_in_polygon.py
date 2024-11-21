import matplotlib.pyplot as plt
import numpy as np
import os

# CHECK IF POINTS ARE IN POLYGON 

## Things to consider
    # - Line intersect algorithm 
    # - Ray casting algorithm 
    # - Winding number algorithm 
    # - 

### Importing data points and polygons
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__)))
data_path = os.path.join(os.path.dirname(ROOT_DIR), "data")

def reading_datapoints(filename, name_parser) -> dict:
    with open(os.path.join(data_path, str(filename)), "r") as f:
        points_lst = f.readlines()
    # reformating point entries  
    for index, points in enumerate(points_lst):
        points_lst[index] = points.replace(",",".").replace("|",",").replace("\n", "")
    #seperating point str from tuple
    points_str = []
    for index, point in enumerate(points_lst):
        points_str.append(point[:name_parser])
        points_lst[index] = point.replace(points_str[index], "").replace("(", "").replace(")", "")
        points_lst[index] = points_lst[index].split(",")
        for i in range(0, len(points_lst[index])):
            points_lst[index][i] =  float(points_lst[index][i])

    points_dict = {points_str[i]:points_lst[i] for i in range(0, len(points_str))}
    return points_dict


## Points
points = reading_datapoints("Points.txt", 2)

## Polygon Points
polygon = reading_datapoints("Polygon.txt", 3)


def drawing_scatter_point(axs, point_name, x, y):
    axs.scatter(x, y, color="k", marker="+")
    axs.text(x+0.3,y, str(point_name))

def is_point_in_polygon(point, polygon):
    """
    Determines if a point is inside a polygon using the Ray-casting algorithm.
    
    :param point: A tuple (x, y) representing the point to test.
    :param polygon: A list of tuples [(x1, y1), (x2, y2), ..., (xn, yn)] representing the polygon's vertices.
    :return: True if the point is inside the polygon, False otherwise.
    """
    x, y = point
    n = len(polygon)
    inside = False
    
    # Loop through all edges of the polygon
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]  # next vertex, with wrap-around
        
        # Check if the point is on an edge (horizontal ray intersects with the edge)
        if min(y1, y2) < y <= max(y1, y2):
            # Compute the x-coordinate of the intersection of the ray with the edge
            x_intersection = (y - y1) * (x2 - x1) / (y2 - y1) + x1
            print("x_intersection result",x_intersection, "x=", x )
            
            # Check if the ray crosses the edge to the right of the point
            if x_intersection > x:
                inside = not inside  # Toggle the inside status
    
    return inside

inside_lst = []
for point in points.values():
    inside_lst.append(is_point_in_polygon(point, list(polygon.values())))

for name, inside in zip(points.keys(), inside_lst):
    print(name, inside)

## creating polygon arrays
x_polygon = []
y_polygon = []
for polygon_point in polygon.values():
    x_polygon.append(polygon_point[0])
    y_polygon.append(polygon_point[1])


figure, axs = plt.subplots()
axs.fill(x_polygon, y_polygon, alpha=0.5, facecolor="none", edgecolor="k")

for point_name, point in zip(points.keys() ,points.values()):
    drawing_scatter_point(axs, point_name, point[0], point[1])
    
plt.show()









