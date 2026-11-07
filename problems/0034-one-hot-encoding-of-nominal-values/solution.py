import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
    if not n_col:
        n_col = len(set(x.tolist()))
        distinct_values = list(set(x.tolist()))
    else:
        distinct_values = [i for i in range(n_col)]

    return [
        [int(distinct_values[j] == x[i]) for j in distinct_values]
        for i in range(x.shape[0])
    ]
