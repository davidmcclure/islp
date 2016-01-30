

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
        self.m = None
        self.b = None

    def least_squares(self):

        mean_x = np.mean(self.x)
        mean_y = np.mean(self.y)

        rise = 0
        run  = 0
        for i in range(len(self.x)):
            rise += (self.x[i]-mean_x) * (self.y[i]-mean_y)
            run  += (self.x[i]-mean_x)**2

        self.m = rise / run
        self.b = mean_y - (self.m*mean_x)

    def plot(self):

        x1 = np.min(self.x)
        x2 = np.max(self.x)

        y1 = self.m*x1 + self.b
        y2 = self.m*x2 + self.b

        plt.scatter(self.x, self.y)
        plt.plot([x1, x2], [y1, y2])

        plt.show()
