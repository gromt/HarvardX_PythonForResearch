# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:09:46 2020

@author: Dmytro Yermolenko
"""

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

n = 500
beta_0 = 5
beta_1 = 2
beta_2 = -1

np.random.seed(1)

x_1 = 10 * ss.uniform.rvs(size=n) # x1 = 0..10
x_2 = 10 * ss.uniform.rvs(size=n)

y = beta_0 + beta_1 * x_1 + beta_2 * x_2 + ss.norm.rvs(loc=0, scale=1, size=n)

X = np.stack([x_1, x_2], axis=1)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:,0], X[:,1], y, c=y)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_zlabel("$y$")

from sklearn.linear_model import LinearRegression
lm = LinearRegression(fit_intercept=True)
lm.fit(X, y)
X_0 = np.array([2, 4])
lm.predict(X_0.reshape(1, -1))
lm.score(X, y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5, random_state=1)
lm = LinearRegression(fit_intercept=True)
lm.fit(X_train, y_train)
lm.score(X_test, y_test)
