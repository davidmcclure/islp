

import matplotlib.pyplot as plt
import numpy as np


class KNN_2d:


    @classmethod
    def from_normal(cls):
        x = np.random.normal(loc=10, scale=2, size=50)
        y = np.random.normal(loc=10, scale=2, size=50)
        return cls(x, y, [])


    def __init__(self, x, y, labels):
        self.x = x
        self.y = y
        self.labels = labels


    def plot(self):
        plt.scatter(self.x, self.y)
        plt.show()
