import numpy as np

def create_dataset():
    cluster1 = np.random.randn(50, 2) + 2
    cluster2 = np.random.randn(50, 2) + 8

    data = np.vstack((cluster1, cluster2))

    return data