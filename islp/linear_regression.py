

import numpy as np
import matplotlib.pyplot as plt


class LinearRegression:

    @classmethod
    def from_line(cls, m=2, b=5, start=0, stop=100, num=100, scale=10):
        x = np.linspace(start, stop, num)
        y = np.random.normal(loc=m*x+b, scale=scale)
        return cls(x, y)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.m = 0
        self.b = 0

    def least_squares(self):

        mean_x = np.mean(self.x)
        mean_y = np.mean(self.y)

        mean_xy = np.mean(self.x * self.y)
        mean_x2 = np.mean(self.x * self.x)

        self.m = (
            (mean_y - (mean_xy / mean_x)) /
            (mean_x - (mean_x2 / mean_x))
        )

        self.b = mean_y - (self.m * mean_x)

    @property
    def rss(self):

        rss = 0
        for i, xi in enumerate(self.x):
            y1 = self.m*xi + self.b
            y2 = self.y[i]
            rss += (y1-y2)**2

        return rss

    def plot(self):

        x1 = np.min(self.x)
        x2 = np.max(self.x)

        y1 = self.m*x1 + self.b
        y2 = self.m*x2 + self.b

        plt.scatter(self.x, self.y)
        plt.plot([x1, x2], [y1, y2])

        plt.show()
