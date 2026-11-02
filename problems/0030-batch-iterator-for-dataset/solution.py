import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
    if y is not None:
        return [
            [X[i: i + batch_size].tolist(), y[i:i+batch_size].tolist()] 
            for i in range(0, X.shape[0], batch_size)
        ]    

    return [
        [X[i: i + batch_size].tolist()] 
        for i in range(0, X.shape[0], batch_size)
    ]    
