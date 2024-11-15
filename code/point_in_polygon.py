import matplotlib.pyplot as plt
import numpy as np
import os

# CHECK IF POINTS ARE IN POLYGON 

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



## Things to consider
    # - Line intersect algorithm 
    # - Ray casting algorithm 
    # - Winding number algorithm 
    # - 







