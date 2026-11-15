
import numpy as np

def rmse(y_true, y_pred):
    # Write your code here

    if y_true.size != y_pred.size or not y_true.size or not y_pred.size:

        raise ValueError("mismatching arrays")



    error_sum = np.sum((y_true - y_pred) ** 2) 

    rmse_res = ((1/y_true.size) * error_sum)**0.5
    return round(rmse_res,3)

