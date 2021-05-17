import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('../data/kmeans_data.csv')

# randomly initalize the centroids
K = 4
centroids = np.random.randn(K, 2)
centroids = centroids * np.std(data, 0)
centroids = centroids + np.mean(data, 0)

for iteration in range(5):
    # assign points to clusters
    deltas = data[:, np.newaxis, :] - centroids
    distances = np.sqrt(np.sum((deltas) ** 2, 2))
    closest = distances.argmin(1)

    # calculate new centroids
    centroids_new = np.array([data[closest == i, :].mean(0) for i in range(K)])
    centroids_new[np.isnan(centroids_new)] = centroids[np.isnan(centroids_new)]
    centroids = centroids_new

# plot
plt.scatter(data[:, 0], data[:, 1], s=40, c=closest)
plt.scatter(centroids[:, 0], centroids[:, 1], c=np.arange(K), s=100)