import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	if len(a) == new_shape[0] and len(a[0]) == new_shape[1]:
		return a

	reshaped_matrix = []

	lst = np.concatenate(a)
	if new_shape[0] * new_shape[1] != len(lst):
		return []
	for i in range(len(lst)):
		if i == 0: 
			reshaped_matrix.append(lst[i:i+2].tolist())
			continue
		if i % new_shape[1] == 0:
			reshaped_matrix.append(lst[i:i+2].tolist())

	return reshaped_matrix