def determinant_3x3(matrix: list[list[int|float]]) -> float:
    det_a = matrix[0][0] * ( matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1] )
    det_b = matrix[0][1] * ( matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0] )
    det_c = matrix[0][2] * ( matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0] )

    return det_a - det_b + det_c



def determinant_4x4(matrix: list[list[int|float]]) -> float:
    a = [
            [matrix[1][0], matrix[1][2], matrix[1][3]],
            [matrix[2][0], matrix[2][2], matrix[2][3]],
            [matrix[3][0], matrix[3][2], matrix[3][3]]
        ]
    b = [
            [matrix[1][1], matrix[1][2], matrix[1][3]],
            [matrix[2][1], matrix[2][2], matrix[2][3]],
            [matrix[3][1], matrix[3][2], matrix[3][3]]
        ]
    c = [
            [matrix[1][1], matrix[1][0], matrix[1][3]],
            [matrix[2][1], matrix[2][0], matrix[2][3]],
            [matrix[3][1], matrix[3][0], matrix[3][3]]
        ]
    d = [
            [matrix[1][1], matrix[1][2], matrix[1][0]],
            [matrix[2][1], matrix[2][2], matrix[2][0]],
            [matrix[3][1], matrix[3][2], matrix[3][0]]
        ]    

    det_a = matrix[0][0] * determinant_3x3(a)
    det_b = matrix[0][1] * determinant_3x3(b)
    det_c = matrix[0][2] * determinant_3x3(c)
    det_d = matrix[0][3] * determinant_3x3(d)

    return det_a + det_b - det_c + det_d