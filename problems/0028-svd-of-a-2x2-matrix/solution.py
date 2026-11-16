

import numpy as np



def svd_2x2(A: np.ndarray) -> tuple:
    print (A)
    print (A.T)

    gram_matrix = np.dot(A.transpose(), A)
    print (gram_matrix)
    trace = gram_matrix.trace()
    determinant = np.linalg.det(gram_matrix)
    # disciminant = trace ** 2 - 4 * 1 * determinant
    disciminant = max(0, trace ** 2 - 4 * 1 * determinant)



    ev_1 = (trace + disciminant ** 0.5) / 2
    ev_2 = (trace - disciminant ** 0.5) / 2
    # print (ev_1)
    # print (ev_2)

    s = [ev_1 ** 0.5, ev_2 ** 0.5]

    # print (s)

    a = gram_matrix[0][0]
    b = gram_matrix[0][1]
    # print (a, b)

    v1 = np.array([b, ev_1 - a])
    v2 = np.array([b, ev_2 - a])
    # print (v1, v2)
    v1_len = ( v1[0] ** 2 + v1[1] ** 2)** 0.5
    v2_len = ( v2[0] ** 2 + v2[1] ** 2)** 0.5
    if v1_len == 0:
        v1_norm = np.array([1.0, 0.0])
    else:
        v1_norm = v1 / v1_len

    if v2_len == 0:
        v2_norm = np.array([0.0, 1.0])
    else:
        v2_norm = v2 / v2_len

    # print (v1_norm, v2_norm)
    u1 = (1 / s[0]) * (A @ v1_norm)
    u2 = (1 / s[1]) * (A @ v2_norm)    
    U = np.column_stack((u1, u2))
    V = np.array([v1_norm, v2_norm])
    # print (u1, u2)
    if V[0, 0] < 0:
        V[0, :] *= -1
        U[:, 0] *= -1
    if V[1, 0] < 0:
        V[1, :] *= -1
        U[:, 1] *= -1


    return U, s, V


