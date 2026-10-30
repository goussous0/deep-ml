import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	standardized_data = np.zeros_like(data, dtype=float)
	normalized_data = np.zeros_like(data, dtype=float)

	for i in range(data.shape[0]):
		for j in range(data.shape[1]):
			x_min = np.min(data[:, j])
			x_max = np.max(data[:, j])
			avg = np.average(data[:, j])
			std = np.std(data[:, j])


			normalized_value = (data[i][j] - x_min)/(x_max - x_min)
			normalized_data[i][j] = normalized_value
			standardized_data[i][j] = (data[i][j] - avg)/std	
	return standardized_data, normalized_data