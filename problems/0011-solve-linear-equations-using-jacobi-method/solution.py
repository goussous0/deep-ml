import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    '''
     x[i] = (1/a_ii) * (b[i] - sum(a_ij * x[j] for j != i))
    '''


    x = [ 0 for _ in range(len(b))]
    lst_shape = np.asarray(A).shape

    for _ in range(n):
        x_new = x.copy()
        for i in range(lst_shape[0]):

                lst = [ A[i][j] * x[j] for j in range(lst_shape[1]) if j != i]

                x_new[i] = (1/A[i][i]) * (b[i] -sum(lst))
        x = x_new

    return [round(item, 4) for item in x]

