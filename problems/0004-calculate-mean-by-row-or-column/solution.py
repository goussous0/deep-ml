def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []


	# col
	if mode.startswith('row'):
		for i in range(len(matrix)):
			means.append(sum (matrix[i]) / len(matrix[i]))

	# row
	elif mode.startswith('column'):
		for col in zip(*matrix):
		    means.append(sum(col)/len(col))	
	return means