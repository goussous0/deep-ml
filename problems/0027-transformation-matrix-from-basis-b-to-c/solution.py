
def det_3x3(m: list[list[int]]):
    det_a = m[0][0] * ( (m[1][1] * m[2][2]) - (m[1][2] * m[2][1]) )
    det_b = m[0][1] * ( (m[1][0] * m[2][2]) - (m[1][2] * m[2][0]) )
    det_c = m[0][2] * ( (m[1][0] * m[2][1]) - (m[1][1] * m[2][0]) )

    return det_a - det_b + det_c

def transpose(m: list[list[int]]):
    t = [
         [0 for i in range(len(m))]
         for i in range(len(m[0]))
    ]
    for i in range(len(m)):
        for j in range(len(m[0])):
            t[j][i] = m[i][j]
    return t

def det(m):
    n = len(m)
    if n == 1:
        return m[0][0]
    total = 0
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in m[1:]]
        total += ((-1) ** j) * m[0][j] * det(minor)
    return total


def adj(m):
    n = len(m)
    C = [[0]*n for _ in range(n)]          # cofactor matrix, fresh storage

    for i in range(n):                      # i = row
        for j in range(n):                  # j = col
            rows = [r for r in range(n) if r != i]
            cols = [c for c in range(n) if c != j]
            minor = [[m[r][c] for c in cols] for r in rows]
            C[i][j] = ((-1) ** (i + j)) * det(minor)

    return transpose(C)                     # adjugate = cofactorᵀ


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    # Create an empty 3x3 result matrix
    result = [
        [0 for i in range(len(a))]
        for j in range(len(b[0]))
    ]
    
    # i loops through rows of 'a'
    for i in range(len(a)):
        # j loops through columns of 'b'
        for j in range(len(b[0])):
            # k loops through the inner dimension
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
            
            result[i][j] = round(result[i][j], 4)
    return result

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    P = []
    det_c = det(C)
    adj_c = adj(C)

    # scalar divide manually 
    for i in range(len(adj_c)):
        for j in range(len(adj_c[0])):
             adj_c[i][j] /= det_c
              


    return matmul(adj_c, B)