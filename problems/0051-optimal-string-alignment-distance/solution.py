import numpy as np
def OSA(source: str, target: str) -> int:
    # Your code here
    '''
        allowed edit operations are:

        - Insert a character
        - Delete a character
        - Substitute a character
        - Transpose two adjacent characters    
    '''

    m = np.zeros((len(source)+1, len(target)+1), dtype=int)

    # filling first row
    for i in range(len(source)+1):
        m[i][0] = i

    for j in range(len(target)+1):
        m[0][j] = j



    for i in range(1, len(source)+1):
        for j in range(1, len(target)+1):

            if source[i-1] == target[j-1]:
                m[i][j] = m[i-1][j-1]
            
            else:
                m[i][j] = 1 + min(m[i-1][j], m[i][j-1], m[i-1][j-1])

                if i > 1 and j > 1:
                    if source[i-1] == target[j-2] and source[i-2] == target[j-1]:
                        m[i][j] = min(m[i][j], m[i-2][j-2]+1)

    return m[len(source)][len(target)]