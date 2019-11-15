from QR_decomp import *

def getSingularValues(A):

    A_T = transpose(A,len(A),len(A[0]))
    AAT = matrix_multiply_matrix(A,A_T,len(A),len(A_T[0]))
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
 
    dim = getMatrixDim(A)
    m = dim[0]
    n = dim[1]
    QR = QR_decomposition(A,len(A),len(A[0]))
    return QR



def fill_R(Q,R):
    result = []
    x = R[0]
    if (len(Q) != len(R[0])):
        for i in range(len(R)):
            temp = []
            for z in range(len(x)):
                temp.append(R[i][z])
            temp.append(0)
            result.append(temp)

            temp = []
        
    else:
        for i in range(len(R)):
            temp = []
            for z in range(len(x)):
                temp.append(R[i][z])
       
            result.append(temp)
      

    return result


    
def repeatQR(A):

    for i in range(50):
        QR = getQR(A)
        Q = QR[0]
        R = QR[1]
        R = fill_R(Q,R)

        if(i == 1):
            print("Q:")
            print_matrix(Q)
            print("R:")
            print_matrix(R)
        
    

        
        A = matrix_multiply_matrix(R,Q,len(R),len(Q[0]))
        #print("Iteration:")
        #print_matrix(A)
    print("\n\nThe Eigenvalues are approximately:")
    print(getMatrixDiag(A))
    return A
 
 
def getEigenValues(A):
    
    A_temp = transpose(A,len(A), len(A[0]))
    A  = matrix_multiply_matrix(A, A_temp,len(A), len(A_temp[0]))
    print_matrix(A)
    iterated_a = repeatQR(A)
    eigenvalues = getMatrixDiag(iterated_a)
    return eigenvalues
 
    
    
    
if __name__ == "__main__":
    #A = [[2,3],[2,4],[1,1]]
    #A = [[2,3, 1], [3,5,1]]
    #A = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
    #A = [[45, 30, -25], [30, -24, 68], [-25, 68, 80]]
    #A = [[2, -1, 1], [1, 3, -2], [0, 1, -2]]
    #A = [[2, 3, 4, 1], [2, 1, 5, 3], [2, 4, 5, 4], [1, 4, 4, 6]]
    #A = [[2, 4, 5], [2, 3, 5], [2, 2, 2], [3, 5, 6], [1, 2, 4]]
    A = [[1, 2], [2, 1], [2,2]]
    #A = [[1, 1, 0, 1], [0, 0, 0, 1], [1, 1, 0, 0]]
   
    #repeatQR(A)
    #getMatrixDiag(A)
    getEigenValues(A)
    #A = [[9,4], [9,16]]
    #getSquareRoots(A)
    #print_matrix(A)
    #repeatQR(A)
    getSingularValues(A)
    
    
    
    
    