import matplotlib.pyplot as plt
import math


p = (-1,0)
d = [p]
dx = .01
th = 0
r = .1


for i in range(50000):
    dth = dx/float(r)
    th += dth
    dpx = r*dth*math.cos(th) +  dx
    dpy = r*dth*math.sin(th)
    p = (p[0]+dpx,p[1]+dpy)
    d.append(p)

xdat = [p[0] for p in d]
ydat = [p[1] for p in d]


plt.plot(xdat,ydat)
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.show()
