import numpy as np
import matplotlib.pyplot as plt

# # # Test poisson dist. generator
# s = np.random.poisson(4,10000)
# count, bins, ignored = plt.hist(s,15,normed=True)
# plt.show()


# def poisson_get_sum(n=5):
# 	return sum([np.random.poisson(3,1)[0] for i in range(n)])

############## uniform example ##############
# def uniform_get_sum(n=5):
# 	data = [np.random.uniform(0,100) for i in range(n)]
# 	return sum(data)

# test_distr = [np.random.uniform(0,100) for i in range(1000)]
# count, bins, ignored = plt.hist(test_distr,50,normed=True)
# plt.show()


# npoints = 10000
# data = [uniform_get_sum() for i in range(npoints)]

# count, bins, ignored = plt.hist(data,50,normed=True)
# plt.show()
################################################




