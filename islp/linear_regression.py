

import numpy as np
import matplotlib.pyplot as plt


class LinearRegression:

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
        plt.scatter(self.x, self.y)
        plt.show()
