import numpy as np

def calculate_correlation_matrix(X, Y=None):
	# Your code here
    if Y is None:
        Y = X
    
    correlation_matrix = np.identity(X.shape[1])


    for i in range(X.shape[1]):
        for j in range(Y.shape[1]):
            x_i = X[:, i]
            y_j = Y[:, j]

            sum_x = sum(x_i)
            sum_y = sum(y_j)
            mean_x = sum_x/X.shape[0]
            mean_y = sum_y/Y.shape[0]

            covariance = 0
            std_x = []
            std_y = []
            for k in range(len(x_i)):
                dst_x = x_i[k] - mean_x
                dst_y = y_j[k] - mean_y
                covariance += dst_x * dst_y
                std_x.append(dst_x**2)
                std_y.append(dst_y**2)


            correlation_matrix[i, j] = covariance / (sum(std_x) * sum(std_y)) ** 0.5

    return correlation_matrix