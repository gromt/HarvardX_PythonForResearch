# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:05:53 2020

@author: Dmytro Yermolenko
"""


import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

n = 100
beta_0 = 5
beta_1 = 2

np.random.seed(1)
x = 10*ss.uniform.rvs(size=n)
y = beta_0 + beta_1 * x + ss.norm.rvs(loc=0, scale=1, size=n)

plt.figure()
plt.plot(x, y, "o", ms=5)
xx = np.array([0,10])
plt.plot(xx, beta_0 + beta_1*xx)
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("fake_regression.pdf")

rss = []
slopes = np.arange(-10, 15, 0.001)
for slope in slopes:
    rss.append(np.sum((y - beta_0 - slope * x)**2))
    
ind_min = np.argmin(rss)
print("Estimate for the slope: ", slopes[ind_min])

plt.figure()
plt.plot(slopes, rss)
plt.xlabel("Slope")
plt.ylabel("RSS")

import statsmodels.api as sm
mod = sm.OLS(y, x)
est = mod.fit()
print(est.summary())

X = sm.add_constant(x)
mod = sm.OLS(y, X)
est = mod.fit()
print(est.summary())
