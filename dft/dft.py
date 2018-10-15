from __future__ import division

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def floor(x):
    return int(str(float(x)).split('.')[0]) # funny floor function

def gauss(x, mu, var):
    pi = np.pi
    return (1/np.sqrt(2*pi*var))*np.exp(-1*(x-mu)**2/var)

def sample_fn(f,rate,xl,xu):
    dx = 1/float(rate)
    x = xl
    xvals = []
    yvals = []
    while x < xu:
        xvals.append(x)
        yvals.append(f(x))
        x+=dx
    return (xvals,yvals)

def pulse(n,width):
    if abs(n)<width/2:
        return 1
    else:
        return 0

def cosine(t,f=None,w=None):
    if f is None and w is None:
        raise Exception('sdfljks')
    if f is None and w is not None:
        return np.cos(t*w)
    if f is not None and w is None:
        return np.cos(2*np.pi*f*t)
    else:
        raise Exception('sdkldlksdlfkj')

def sawtooth(t,f):
    if abs(t)<.0001:
        return 0.0
    t = t*f
    tf = math.floor(t)
    return t-tf


def square(t,f):
    q = 1 if t>0 else -1
    t = t*f
    dec = float('.'+str(float(t)).split('.')[-1])
    if dec*q>.5*q:
        return 0
    else:
        return 1

def Cexp(val):
    if val > 0:
        return Cx(math.cos(val),math.sin(val))
    elif val == 0:
        return Cx(1,0)
    else:
        return Cx(math.cos(-1*val),-1*math.sin(-1*val))

    return Cx()

def sum_list(L):
    j = Cx(0,0)
    for k in L:
        j = j.add(k)
    return j



class Cx(object):
    def __init__(self,real, imag):
        self.r = real
        self.i = imag

    def __str__(self):
        if self.i >=0:
            o='+'
        else:
            o=''
        return "{0}{1}{2}i".format(self.r,o,self.i)

    def mag(self):
        return np.sqrt(self.i**2+self.r**2)

    def add(self, xi):
        if type(xi) is Cx:
            return Cx(self.r+xi.r,self.i+xi.i)
        else:
            return Cx(self.r+xi,self.i)

    def mult(self,xi):
        if type(xi) is Cx:
            return Cx(self.r*xi.r-self.i*xi.i,self.r*xi.i+self.i*xi.r)
        else:
            return Cx(self.r*xi,self.i*xi)



def dft(x=None,y=None):
    if x is None or y is None:
        raise Exception('dslkjfdslkjsdfklj')

    sample_rate = 1/abs(x[0]-x[1])
    pairs = [(x[i],y[i]) for i in range(len(x))]
    N = float(len(pairs))
    F = []
    v = []

    for k in range(int(len(pairs)/2)):
        # params
        pair = pairs[k]
        tx = pair[0]
        ty = pair[1]

        # compute series
        dft_series = []
        for j in range(len(pairs)):
            p = pairs[j]
            xp = p[0]
            yp = p[1]
            dft_series.append(Cexp(-1*2*np.pi*k*j/N).mult(yp))

        # sum and append
        F.append(sum_list(dft_series).mag())
        v.append(k*sample_rate/N)

    return (v,F)


if __name__=='__main__':
    sample_rate = 30
    # f = lambda x: 100*gauss(x, mu=3,var=.08)
    f = lambda x: 5*cosine(x, f=1.5) + 30*cosine(x,f=3) + 15*cosine(x,f=4)
    # f = lambda x: pulse(x,width=5)

    x,y = sample_fn(f,sample_rate,0,sample_rate/2)
    v,F = dft(x,y)



    x = np.array(x)


    y = np.array(y)
    F = np.array(F)

    F = F/max(F)
    y = y/max(y)


    plt.plot(x,y,'r',v,F,'b')
    # plt.xlim(0,10)
    # plt.ylim(-10,15)
    plt.show()
