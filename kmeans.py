import numpy as np


def assign_clusters(data, centroids):

    differences = data[:, np.newaxis] - centroids

    squared = differences ** 2

    sum_squared = np.sum(squared, axis=2)

    distances = np.sqrt(sum_squared)

    labels = np.argmin(distances, axis=1)

    return labels


def update_centroids(data, labels, k):

    new_centroids = np.zeros((k, 2))

    for i in range(k):

        cluster_points = data[labels == i]

        centroid = np.mean(cluster_points, axis=0)

        new_centroids[i] = centroid

    return new_centroids


def kmeans(data, k, max_iters=100):

    random_indices = np.random.choice(data.shape[0], k, replace=False)

    centroids = data[random_indices]

    for _ in range(max_iters):

        labels = assign_clusters(data, centroids)

        new_centroids = update_centroids(data, labels, k)

        if np.allclose(centroids, new_centroids):
            break

        centroids = new_centroids

    return centroids, labels