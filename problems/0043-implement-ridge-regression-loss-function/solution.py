import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    # Your code here

    predictions = X @ w
    errors = predictions - y_true

    squared_errors = np.square(errors)     
    # print (np.square(errors))
    sum_squared_errors = sum(squared_errors)


    squared_weights = np.square(w)
    sum_squared_weights = sum(squared_weights)


    return sum_squared_errors/X.shape[0] + sum_squared_weights * alpha