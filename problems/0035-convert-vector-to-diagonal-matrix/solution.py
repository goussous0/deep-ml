import numpy as np

def make_diagonal(x):
	# Your code here
	arr = np.zeros(shape=(x.shape[0], x.shape[0]))
	for i in range(x.shape[0]):
		arr[i][i] = x[i]
	
	return arr
