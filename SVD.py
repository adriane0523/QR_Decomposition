from QR_decomp import*

def getSingularValues(A):
    
    dim = getMatrixDim(A)
    m = dim[0]
    n = dim[1]
    A_T = transpose(A,m,n)
    AAT = matrix_multiply_matrix(A,A_T,m,n)
    eig = getEigenValues(AAT)
    sqrts = []
    for i in eig:
        sqrt = i**(0.5)
        sqrts.append(sqrt)
    print(sqrts)
    return sqrts

def getSingularMatrix(A):
    sing = getSingularValues(A)
    count = 0
    length = len(sing)
    sing_matrix = A
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i == j:
                sing_matrix[i][j] = sing[count]
                count = count+1
            else:
                sing_matrix[i][j] = 0
    print_matrix(sing_matrix)
    return sing_matrix
    

    
def getMatrixDim(A):
    m = 0
    n = 0
    for i in range(len(A)):
        m = m+1
    for j in range(len(A[0])):
        n = n+1
    ans = [m, n]
    return ans
    
def getMatrixDiag(A):
    diag = []
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i==j:
                diag.append(A[i][j])
    return diag
    
def getQR(A):
    from QR_decomp_real import QR_decomposition_noprint
    dim = getMatrixDim(A)
    m = dim[0]
    n = dim[1]
    QR = QR_decomposition_noprint(A,m,n)
    return QR

    
def repeatQR(A):
    QR = getQR(A)
    Q = QR[0]
    R = QR[1]
    dim = getMatrixDim(R)
    m = dim[0]
    n = dim[1]
        
    for i in range(1000):
        QR = getQR(A)
        Q = QR[0]
        R = QR[1]
        A = matrix_multiply_matrix(R,Q,m,n)
    
    print_matrix(A)
    return A
    #print("\n\nThe Eigenvalues are approximately:")
    #print(getMatrixDiag(A))
 
def getEigenValues(A):
    iterated_a = repeatQR(A)
    eigenvalues = getMatrixDiag(iterated_a)
    print("The eigenvalues:")
    print(eigenvalues)
    return eigenvalues
 
    
    
    
if __name__ == "__main__":
    #A = [[2,3],[2,4],[1,1]]
    #A = [[2,3, 1], [3,5,1]]
    #A = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
    A = [[45, 30, -25], [30, -24, 68], [-25, 68, 80]]
    #A = [[2, -1, 1], [1, 3, -2], [0, 1, -2]]
    #A = [[2, 3, 4, 1], [2, 1, 5, 3], [2, 4, 5, 4], [1, 4, 4, 6]]
    #A = [[2, 4, 5], [2, 3, 5], [2, 2, 2], [3, 5, 6], [1, 2, 4]]
    #repeatQR(A)
    #getMatrixDiag(A)
    #getEigenValues(A)
    #A = [[9,4], [9,16]]
    #getSquareRoots(A)
    #print_matrix(A)
    repeatQR(A)
    
    
    
    