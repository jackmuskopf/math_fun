import random
import numpy as np
import matplotlib.pyplot as plt

def sum_vecs(L):
    return [sum([L[i][j] for i in range(len(L))]) for j in range(len(L[0]))]
    # return [v1[i]+v2[i] for i in range(len(v1))]

ds = []
n = 9900
for j in range(8):
    print('...')
    d = [0]
    for i in range(n):
        d.append(d[i]+2*int(random.randrange(0,2))-1)

    ds.append(np.array(d))

x = [-1]+list(range(n))

avg = np.array(sum_vecs(ds))/float(len(ds))
plt.plot(x,avg,'o')
c = {0:'b',1:'r',2:'k',3:'g'}
for i in range(len(ds)):
    plt.plot(x,ds[i],c[i%4])
plt.show()
