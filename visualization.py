import matplotlib.pyplot as plt


def visualize(data, labels, centroids):

    plt.scatter(data[:, 0], data[:, 1], c=labels)

    plt.scatter(
        centroids[:, 0],
        centroids[:, 1],
        color="red",
        marker="X",
        s=200
    )

    plt.show()