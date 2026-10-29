import math


def sigmoid(x):
	return  1 / (1 + math.pow(math.e, -x))


def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	probabilities = []
	errors = []
	for i in range(len(features)): # loop over features
		value = sum([ weights[j] * features[i][j] for j in range(len(features[i]))]) + bias
		probability = round(sigmoid(value), 4)
		probabilities.append(probability)

		errors.append(math.pow(labels[i] - probability, 2))	
	mse = 1/len(features) * sum(errors)
	return probabilities, mse
