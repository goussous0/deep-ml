import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True):
    # Your code here
    n = X.shape[0]
    subset_size = n if replacements is True else n//2 

    lst = []
    for i in range(n_subsets):
        indices = np.random.choice(n, subset_size, replace=replacements)
        lst.append((X[indices], y[indices]))
        # print (X[indices])
        # print (y[indices])
    return lst
