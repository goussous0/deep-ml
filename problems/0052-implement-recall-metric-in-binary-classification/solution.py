import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    # Your code here
    tp = 0
    fn = 0
    for i in range(y_true.shape[0]):

        if y_pred[i] == y_true[i] and y_pred[i] > 0:
            tp += 1
        
        elif y_pred[i] == 0 and y_true[i] == 1:
            fn += 1

    if tp == 0 and fn == 0: return 0

    return tp / (tp + fn)

