import numpy as np

def kernel_function(x1, x2):
	# Your code here
	return sum(
		[x1[i] * x2[i] for i in range(x1.shape[0])]
	)

