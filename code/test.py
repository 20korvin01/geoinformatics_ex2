import numpy as np
import matplotlib.pyplot as plt


# generate 200 random data points with id
data = np.random.randint(0, 10000, (200, 2))
data = np.hstack((np.arange(1, 201).reshape(-1, 1), data))

# plot the data
plt.scatter(data[:, 1], data[:, 2])
plt.show()

