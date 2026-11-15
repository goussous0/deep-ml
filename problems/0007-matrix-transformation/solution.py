
import numpy as np


def determinant(m: list[list[int|float]]):
    # det = (m[0][0] * m[1][1]) - (m[0][1] * m[1][0] ) # hardcoded 2x2 matrix
    return np.linalg.det(m)



def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

    transformed_matrix = []

    if determinant(T) == 0 or determinant(S) == 0:
        return -1


    A = np.array(A)
    T = np.array(T)
    S = np.array(S)


    return np.linalg.inv(T) @ A @ S