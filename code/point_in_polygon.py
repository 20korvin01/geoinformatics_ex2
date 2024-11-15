import matplotlib.pyplot as plt
import numpy as np
import sys
import os

### Importing data points and polygons
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__)))
data_path = os.path.join(os.path.dirname(ROOT_DIR), "data")

with open(os.path.join(data_path, "Points.txt"), "r") as f:
    points_lst = f.readlines()
# reformating point entries  
for index, points in enumerate(points_lst):
    points_lst[index] = points.replace(",",".").replace("|",",").replace("\n", "")


#seperating point str from tuple
points_str = []
for index, point in enumerate(points_lst):
    points_str.append(point[:2])
    points_lst[index] = point.replace(points_str[index], "").replace("(", "").replace(")", "")
    points_lst[index] = points_lst[index].split(",")
    for i in range(0, len(points_lst[index])):
        points_lst[index][i] =  float(points_lst[index][i])


print(points_lst)

