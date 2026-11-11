import numpy as np

def sigmoid(score):
    return 1 / ( 1 + np.exp(-score))

def loss(prediction, label):
    return  ((prediction - label)**2)

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) :
    # Your code here
    mse_values = []
    weights = initial_weights.copy()
    bias = initial_bias

    for k in range(epochs):
        # linear function 
        epoch_loss = 0
        total_grad_w = [0.0] * len(weights)
        total_grad_b = 0.0        
        for i in range(len(features)): # loop over samples

            score = sum([ (weights[j] * features[i][j])   for j in range(len(weights))]) + bias
            prediction = sigmoid(score)
            error = loss(prediction, labels[i])

            epoch_loss += error

            # back propagation
            delta = 2 * (prediction - labels[i]) * prediction * (1 - prediction)
            # 2. Accumulate the gradients
            total_grad_b +=  delta
            for j in range(len(weights)):
                total_grad_w[j] +=  delta * features[i][j]


        # 3. Update ONCE per epoch (after the sample loop)
        for j in range(len(weights)):
            # Divide by len(features) to get the average gradient
            weights[j] = weights[j] - (learning_rate * (total_grad_w[j] / len(features)))
            
        bias = bias - (learning_rate * (total_grad_b / len(features)))

        # Record MSE
        mse_values.append(round(epoch_loss / len(features), 4)) 
    
    
    return ([round(weight, 4) for weight in weights], round(bias, 4), mse_values)