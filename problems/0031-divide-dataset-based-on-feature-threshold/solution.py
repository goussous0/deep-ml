import numpy as np

def divide_on_feature(X, feature_i, threshold):
    # Your code here
    include = []
    exclude = []

    for i in range(X.shape[0]):
        if X[i][feature_i] < threshold:
            include.append(X[i].tolist())
        else:
            exclude.append(X[i].tolist())

    return [np.array(exclude), np.array(include)]