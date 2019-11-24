def transposeMatrix(M):
    rows = len(M); cols = len(M[0])

    MT = [[0 for x in range(len(M))] for y in range(len(M[0]))]

    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]

    return MT

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def multiply(A, B):
    rowsA = len(A); colsA = len(A[0])
    rowsB = len(B); colsB = len(B[0])
    
    if colsA != rowsB:
        raise ArithmeticError(
            'Number of A columns must equal number of B rows.')

    C = [[0 for x in range(colsB)] for y in range(rowsA)]
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = [[0 for x in range(len(m))] for y in range(len(m))]
    for r in range(len(m)):
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactors[r][c] = ((-1)**(r+c)) * getMatrixDeternminant(minor)
            #cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        #cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


