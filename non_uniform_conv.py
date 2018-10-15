from __future__ import division
import numpy as np
import math
import matplotlib.pyplot as plt

xvals = np.arange(0,1.005,.001)

ysets = []
# for n in np.arange(1,1000,5):
#     ys = [x**n/(1+x**n) for x in xvals]
#     ysets.append(ys)

for n in np.arange(1,1000,5):
    ys = [math.sin(x**n) for x in xvals]
    ysets.append(ys)

colors = ['k','g','b','r']

for j in range(len(ysets)):
    cs = j%4
    plt.plot(xvals,ysets[j],colors[cs])
plt.show()
