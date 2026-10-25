import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	x_ = np.array(X, dtype=float)
	y_ = np.array(y, dtype=float)
	x_transpose = x_.T

	theta = np.linalg.inv(x_transpose @ x_) @ x_transpose @ y_

	return np.round(theta, 4).tolist()