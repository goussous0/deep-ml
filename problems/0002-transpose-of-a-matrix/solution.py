def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    b = []
    m = len(a)
    n = len(a[0])

    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(a[j][i])
        b.append(tmp)
    return b