import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    tr  = matrix[0][0] + matrix[1][1]


    # D = b² - 4ac
    descrim = tr**2  - 4 * det
    if descrim < 0:
        return None

    # x^2 - tr * x + det = 0 


    return [
        (tr  + math.sqrt(descrim))/2,
        (tr  - math.sqrt(descrim))/2
    ]
