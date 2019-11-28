def determinant(A):
    n = len(A)
    AM = copyMatrix(A)

    for fd in range(n):
        if AM[fd][fd] == 0: 
            AM[fd][fd] = 1.0e-18
        for i in range(fd+1,n): 
            crScaler = AM[i][fd] / AM[fd][fd] 
            for j in range(n): 
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
    
    product = 1.0
    for i in range(n):
        product *= AM[i][i]

    return product

def getMatrixInverse(A, tol=None):
    checkIfSquareMatrix(A)
    checkIfNonSingular(A)

    n = len(A)
    AM = copyMatrix(A)
    I = identityMatrix(n)
    IM = copyMatrix(I)

    indices = list(range(n))
    for fd in range(n):
        fdScaler = 1.0 / AM[fd][fd]
        for j in range(n):
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        for i in indices[0:fd] + indices[fd+1:]: 
            crScaler = AM[i][fd] 
            for j in range(n): 
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

    if checkIfEqual(I, multiply(A,IM),tol):
        return IM
    else:
        raise ArithmeticError("Error in finding inverse")

def zerosMatrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M

def identityMatrix(n):
    I = zerosMatrix(n, n)
    for i in range(n):
        I[i][i] = 1.0

    return I

def copyMatrix(M):
    rows = len(M); cols = len(M[0])
    MC = zerosMatrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC

# printMatrix(M, decimals=3):
#    for row in M:
#        print([round(x,decimals)+0 for x in row])

def transposeMatrix(M):
    if not isinstance(M[0],list):
        M = [M]

    rows = len(M); cols = len(M[0])

    MT = zerosMatrix(cols, rows)

    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]

    return MT

def multiply(A, B):
    rowsA = len(A); colsA = len(A[0])
    rowsB = len(B); colsB = len(B[0])
    if colsA != rowsB:
        raise ArithmeticError(
            'Number of A columns must equal number of B rows.')

    C = zerosMatrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C

def checkIfEqual(A, B, tol=None):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False

    for i in range(len(A)):
        for j in range(len(A[0])):
            if tol == None:
                if A[i][j] != B[i][j]:
                    return False
            else:
                if round(A[i][j],tol) != round(B[i][j],tol):
                    return False

    return True

def checkIfSquareMatrix(A):
    if len(A) != len(A[0]):
        raise ArithmeticError("Not a square matrix, inverese cant be found")



def checkIfNonSingular(A):
    det = determinant(A)
    if det != 0:
        return det
    else:
        raise ArithmeticError("Matrix is singular")