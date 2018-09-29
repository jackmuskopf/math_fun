
import operator
import itertools
from itertools import chain, combinations
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return
    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset
        yield [ [ first ] ] + smaller
primes = get_primes(50000)
# primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
def prime_factor(n):
    return [p for p in primes if p<=n and n%p==0]
def multiply_list(l):
    j = 1
    for i in l:
        j = j*i
    return j
def method4():
    '''
    does not fill out pattern from top down,
    something wrong here? get assertion error
    '''
    _primes = get_primes(30)
    subsets = [s for s in powerset(_primes) if s and s!=_primes]
    x = []
    y = []
    for s in subsets:
        compliment = [j for j in _primes if j not in s]
        c_subs = [p for p in powerset(compliment) if p]
        c_subs.append([1])
        for c in c_subs:
            a = multiply_list(s)
            b = multiply_list(c)
            print(a,b)
            if b > a:
                x.append(a/float(b))
                y.append(1/float(b))
            else:
                x.append(b/float(a))
                y.append(1/float(a))
            if 0.0 in y:
                assert False
    assert len(set(y)) == len(y)
    plt.plot(x, y, 'bo')
    print(len(x))
    plt.show()
def method3():
    parts = list(partition(get_primes(25)))
    [p.append([1]) for p in parts]
    x = []
    y = []
    for part in parts:
        pairs = list(itertools.combinations(part,2))
        for pair in pairs:
            a = multiply_list(pair[0])
            b = multiply_list(pair[1])
            print(a,b)
            if b > a:
                x.append(a/float(b))
                y.append(1/float(b))
            else:
                x.append(b/float(a))
                y.append(1/float(a))
    plt.plot(x, y, 'bo')
    print(len(x))
    plt.show()
def method2():
	'''
	pretty fills in from top down
	'''
	points = 500
	x = [.5,]
	y = [.5,]
	d = 2
	pf_denominator = prime_factor(d)
	e = 1/float(points)
	count = 0
	while count < points:
		i = 1
		while count < points and i < d:
			# for i in range(1,d-1):
			xn = i/float(d)
			pf_numerator = prime_factor(i)
			intersection = [p for p in pf_numerator if p in pf_denominator]
			if not intersection:
				# if min([abs(j - xn) for j in x]) > .0000001:
				x.append(xn)
				y.append(1/float(d))
			else:
				pass
			i+=1
		count+=1
		d += 1
		pf_denominator = prime_factor(d)
		print(count/float(points))

	pairs = [(x[i],y[i]) for i in range(len(x))]
	print('here')
	colors = cm.rainbow(np.linspace(0, 1, len(pairs)))
	for y, c in zip(pairs, colors):
		plt.scatter(y[0], y[1], color=c)
	# plt.plot(x, y, 'bo')
	plt.show()

def method1():
    # number of points to plot
    npoints = 100000
    powers = range(10)
    # find good power
    best = { i : abs(2^i - npoints) for i in powers}
    # max(stats.iteritems(), key=operator.itemgetter(1))[0]
    #
    # find demoninators of rationals
    #
    power = 1
    data = [[],[]]
    while len(data[0]) < npoints:
        d = 2**power
        print(d)
        # for i in range(1,d):
        #     x = i/float(d)
        #     y = 1/float(d)
        #     if y >
        x = [i/float(d) for i in range(1,d)]
        y = [1/float(d) for i in range(1,d)]
        data[0] += x
        data[1] += y
        power += 1
    plt.plot(data[0],data[1], 'bo')
    plt.show()

if __name__=='__main__':
	method2()
