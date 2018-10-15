from pybrary.complex import *


def split_list(my_list):
	# split list into two lists, odd indices and even indices
    	_x = my_list
    	switch = True
    	x_odd = []
    	x_even = []
    	while _x:
    		if switch:
    			x_odd.append(_x.pop(0))
    		else:
    			x_even.append(_x.pop(0))
    		switch = not switch
    	return (x_odd,x_even)

def is_power(N,x):
	# returns truth of : "N is a power of x"
	if (type(N),type(x)) != (int,int):
		raise Exception('is_power() takes two ints!')
	while N > 1:
		if N%x != 0:
			return False
		else:
			N = N/x
	return True

# X0,...,N−1 ← ditfft2(x, N, s):             DFT of (x0, xs, x2s, ..., x(N-1)s):
#     if N = 1 then
#         X0 ← x0                                      trivial size-1 DFT base case
#     else
#         X0,...,N/2−1 ← ditfft2(x, N/2, 2s)             DFT of (x0, x2s, x4s, ...)
#         XN/2,...,N−1 ← ditfft2(x+s, N/2, 2s)           DFT of (xs, xs+2s, xs+4s, ...)
#         for k = 0 to N/2−1                           combine DFTs of two halves into full DFT:
#             t ← Xk
#             Xk ← t + exp(−2πi k/N) Xk+N/2
#             Xk+N/2 ← t − exp(−2πi k/N) Xk+N/2
#         endfor
#     endif

def fft(x, N, s):
	if type(N) is not int:
		raise Exception('N needs to be int in fft()')
	if not is_power(N,2):
		raise Exception('This fft implementation takes only samples of size 2^n')
    if N == 1:
        return x
    else:
    	x_odd, x_even = split_list(x)
    	fft_odd = fft(x_odd,len(x_odd),s*2)
    	fft_even = fft(x_even,len(x_even),s*2)
    	Xt = fft_odd+fft_even
    	for k in range(N/2):
    		t = Xt[k]
    		Xt[k] = t + math.exp()



    		

