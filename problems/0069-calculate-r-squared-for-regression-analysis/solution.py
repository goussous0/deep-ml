
import numpy as np

def r_squared(y_true, y_pred):
    # Write your code here
    mean_y_true = sum(y_true)/y_true.shape[0]

    rss = 0
    tss = 0

    for i in range(y_true.shape[0]):
        rss += (y_true[i] - y_pred[i])**2
        tss += (y_true[i] - mean_y_true)**2
    
    return 1 - (rss / tss)

