#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:42:37 2024

@author: nishi
"""

import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import CubicSpline


x = np.linspace(0, 10, num=11)
y = np.cos(-x**2 / 9.0)


xnew = np.linspace(0, 10, num=1001)
ynew = np.interp(xnew, x, y)

spl = CubicSpline(x, y)

plt.plot(xnew, ynew, '-', label='linear interp')
plt.plot(x, y, 'o', label='data')
plt.legend(loc='best')

plt.show()

fig, ax = plt.subplots(4, 1, figsize=(5, 7))
xnew = np.linspace(0, 10, num=1001)

ax[0].plot(xnew, spl(xnew))
ax[0].plot(x, y, 'o', label='data')
ax[1].plot(xnew, spl(xnew, nu=1), '--', label='1st derivative')
ax[2].plot(xnew, spl(xnew, nu=2), '--', label='2nd derivative')
ax[3].plot(xnew, spl(xnew, nu=3), '--', label='3rd derivative')

for j in range(4):
    ax[j].legend(loc='best')
plt.tight_layout()

plt.show()