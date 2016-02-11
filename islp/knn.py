

import matplotlib.pyplot as plt

from sklearn.datasets.samples_generator import make_blobs


# TODO
# plot response colors
# given x/y/k, predict a level


class KNN_2d:


    @classmethod
    def from_blobs(cls):

        X, y = make_blobs(
            n_samples=1000,
            centers=5,
            cluster_std=1,
            n_features=5,
        )

        return cls(X, y)


    def __init__(self, X, y):
        self.X = X
        self.y = y


    def plot(self):
        plt.scatter(self.X[:, 0], self.X[:, 1])
        plt.show()
