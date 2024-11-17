import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

# Function to handle triangle highlighting
def on_click(event, points, tri):
    if event.inaxes is not None:
        # Get the click location
        click_point = np.array([event.xdata, event.ydata])

        # Check which triangle the click is inside
        for triangle_index, simplex in enumerate(tri.simplices):
            # Get the vertices of the triangle
            vertices = points[simplex]
            
            # Use barycentric coordinates to check if point is inside triangle
            A = np.array([
                [vertices[0][0], vertices[0][1], 1],
                [vertices[1][0], vertices[1][1], 1],
                [vertices[2][0], vertices[2][1], 1],
            ])
            b = np.array([click_point[0], click_point[1], 1])
            
            # If the determinant of A-b is non-negative, point is inside triangle
            bary_coords = np.linalg.solve(A.T, b)
            if np.all(bary_coords >= 0) and np.sum(bary_coords) == 1:
                # Highlight the triangle
                plt.gca().cla()
                plt.triplot(points[:, 0], points[:, 1], tri.simplices, color="gray", alpha=0.5)
                plt.fill(vertices[:, 0], vertices[:, 1], color="yellow", alpha=0.5)

                # Annotate the selected triangle
                centroid = np.mean(vertices, axis=0)
                plt.text(centroid[0], centroid[1], str(triangle_index), color="red", fontsize=12, ha='center', va='center')
                
                # Annotate vertices
                for vertex_index, (x, y) in zip(simplex, vertices):
                    plt.text(x, y, str(vertex_index), color="blue", fontsize=10, ha='center', va='bottom')
                
                # Redraw the plot
                plt.plot(points[:, 0], points[:, 1], 'o', color="blue")  # Blue points
                plt.title("Click on a Triangle")
                plt.draw()
                break

# Function for Delaunay triangulation
def delaunay_triangulation(points):
    tri = Delaunay(points)
    
    # Plot the triangulation with initial colors
    fig, ax = plt.subplots()
    plt.triplot(points[:, 0], points[:, 1], tri.simplices, color="gray", alpha=0.5)  # Gray lines
    plt.plot(points[:, 0], points[:, 1], 'o', color="blue")  # Blue points
    plt.title("Click on a Triangle")
    
    # Connect the click event
    fig.canvas.mpl_connect('button_press_event', lambda event: on_click(event, points, tri))
    plt.show()

    # Point and Triangle List
    points_list = np.concatenate((np.arange(points.shape[0])[:, None], points), axis=1)
    triangles_list = np.concatenate((np.arange(tri.simplices.shape[0])[:, None], tri.simplices), axis=1)
    
    print("Point List:")
    print(points_list)
    print("\nTriangulation:")
    print(triangles_list)

if __name__ == "__main__":
    # Generate a set of 200 2D points with random X and Y coordinates in [0, 10000]
    points = np.random.randint(0, 10000, (200, 2))
    
    # Call the function    
    delaunay_triangulation(points)
