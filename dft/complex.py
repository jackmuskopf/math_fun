import math

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

def Cexp(val):
    if val > 0:
        return Cx(math.cos(val),math.sin(val))
    elif val == 0:
        return Cx(1,0)
    else:
        return Cx(math.cos(-1*val),-1*math.sin(-1*val))

    return Cx()
                