import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
import pywt
import pywt.data


# Load image
original = pywt.data.camera()


def example1():
	# Wavelet transform of image, and plot approximation and details
	titles = ['Approximation', ' Horizontal detail',
	          'Vertical detail', 'Diagonal detail']
	coeffs2 = pywt.dwt2(original, 'bior1.3')
	(LL, (LH, HL, HH)) = coeffs2

	recon = pywt.idwt2(coeffs2,'bior1.3','smooth')

	print(np.linalg.norm(recon-original))
	assert False

	# recon = None
	# for M in [LL, LH, HL, HH]:
	# 	if recon is None:
	# 		recon = M
	# 	else:
	# 		recon

	fig = plt.figure(figsize=(12, 3))
	for i, a in enumerate([LL, LH, HL, HH]):
	    ax = fig.add_subplot(1, 4, i + 1)
	    ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
	    ax.set_title(titles[i], fontsize=10)
	    ax.set_xticks([])
	    ax.set_yticks([])



	fig.tight_layout()
	plt.show()


x = original.flatten()
d = int(len(x))

if d%2 != 0:
	raise Exception('Length exception')


dby2 = d//2

print(dby2)
assert False

haar_block = np.matrix([[.5, -.5],[.5, .5]])
_W = [haar_block]*dby2
W = linalg.block_diag(*_W)

xhat = W*x

