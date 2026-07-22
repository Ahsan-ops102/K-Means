from dataset import create_dataset
from kmeans import kmeans
from visualization import visualize


def main():

    data = create_dataset()

    centroids, labels = kmeans(data, k=2)

    print("Final Centroids:")
    print(centroids)

    visualize(data, labels, centroids)


if __name__ == "__main__":
    main()