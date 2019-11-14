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
    
# def getSquareRoots(A):
    # ans = 0
    # sqrts = []
    # sqrts_row = []
    # row = []
    # count_row = 0
    # count_column = 0
    # for i in A:
        # row.append(i)
        # for j in A[0]:
            
    # print(row)
    
def vector_divide_mag(vector_1, magnitude):
    result = []
    for i in vector_1:
        result.append((float)(i/magnitude))

    return result

def dot(vector_1, vector_2):
    result = 0
    count = 0
    for i in vector_1:
        result = float(result + (float)(i * vector_2[count]))
        count = count + 1
    return result
    
def get_magnitude_vector(vector_1):
    result = 0
    for i in vector_1:
        result = result + (float)(i**2)
    
    return (float)(result**(1/2))
 
def vector_add_vector(vector_1, vector_2):
    result = []
    for i in range(len(vector_1)):
        
            result.append(vector_1[i] + vector_2[i])
    return result
    
def vector_multiply_num(vector_1,num):
    result = []
    for i in vector_1:
        result.append((float)(i * num))

def transpose(matrix, m, n):
    
    result = []
    row = []
    for i in range(n):
        for x in range(m):
            row.append(0)
        
        result.append(row)
        row = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result

def matrix_multiply_matrix(matrix_1, matrix_2, m, n):
    result = []
    row = []
    for i in range(n):
        for x in range(m):
            row.append(0)
        
        result.append(row)
        row = []
    
        # iterating by row of A 
    for i in range(len(matrix_1)): 
    
        # iterating by column by B  
        for j in range(len(matrix_2[0])): 
    
            # iterating by rows of B 
            for k in range(len(matrix_2)): 
                result[i][j] += matrix_1[i][k] * matrix_2[k][j] 
    return result
    
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
    from QR_decomp import QR_decomposition
    dim = getMatrixDim(A)
    m = dim[0]
    n = dim[1]
    QR = QR_decomposition(A,m,n)
    return QR

def print_matrix(A):
    print("______________________________\n")
    for i in A:
        print('      ', i)
    print("______________________________\n")
    
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
    #print("Iteration:")
    #print_matrix(A)
    #print("\n\nThe Eigenvalues are approximately:")
    #print(getMatrixDiag(A))
    return A
 
 
def getEigenValues(A):
    iterated_a = repeatQR(A)
    eigenvalues = getMatrixDiag(iterated_a)
    #print("The eigenvalues:")
    print(eigenvalues)
    return eigenvalues
 
    
    
    
if __name__ == "__main__":
    #A = [[2,3],[2,4],[1,1]]
    #A = [[2,3, 1], [3,5,1]]
    #A = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
    #A = [[45, 30, -25], [30, -24, 68], [-25, 68, 80]]
    #A = [[2, -1, 1], [1, 3, -2], [0, 1, -2]]
    #A = [[2, 3, 4, 1], [2, 1, 5, 3], [2, 4, 5, 4], [1, 4, 4, 6]]
    #A = [[2, 4, 5], [2, 3, 5], [2, 2, 2], [3, 5, 6], [1, 2, 4]]
    #A = [[1, 2], [2, 1]]
    A = [[1, 1, 0, 1], [0, 0, 0, 1], [1, 1, 0, 0]]
    #repeatQR(A)
    #getMatrixDiag(A)
    getEigenValues(A)
    #A = [[9,4], [9,16]]
    #getSquareRoots(A)
    #print_matrix(A)
    #repeatQR(A)
    #getSingularValues(A)
    
    
    
    
    