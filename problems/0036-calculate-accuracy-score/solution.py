import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	true = 0
	for i in range(y_true.shape[0]):
		true += int(y_true[i] == y_pred[i])


	return true/y_true.shape[0]