from QR_decomp import *
from rreftest import *
from Inverse import  *


def getSingularValues(vectors):

    #A_T = transpose(A,len(A),len(A[0]))
    #AAT = matrix_multiply_matrix(A,A_T,len(A),len(A_T[0]))
    eig = vectors
    sqrts = []
    for i in eig:
        sqrt = i**(0.5)
        sqrts.append(sqrt)
    print("Singular Values")
    print(sqrts)
    return sqrts

def getSingularMatrix(A, lambdas):
    result = []
    count = 0
    for i in range(len(lambdas)):
        temp = []
        for k in range(len(lambdas)):
            if k == count:
                temp.append(lambdas[count])
            else:
                temp.append(0)
        result.append(temp)
        temp = []
        count +=1





    return result
    
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
   # print(getMatrixDiag(A))
    return A

def getEigenVectors(A, eigenvalues):
    result = []
    eignvalues_matrix =  []

    if len(A) != len(A[0]):
        A = matrix_multiply_matrix(A, transpose(A, len(A), len(A[0])),len(A), len(A))

    count = 0
    for i in range(len(eigenvalues)):
        e_vector = []
        diag = 0
        for x in range(len(A)):
            temp = []
        
            for z in range(len(A[0])):
                if diag == z:
                    
                    temp.append(A[x][z] - eigenvalues[count])
                else:
                    temp.append(A[x][z])
            diag += 1
            e_vector.append(temp) 
            temp = []

        count += 1
        #print("BEFORE rref")
        #print_matrix(e_vector) 
        e_vector = rref(e_vector)
       # print("rref:")
        #print_matrix(e_vector)
        result.append(e_vector)


        eignvalues_matrix.append(solve_eignvalues(e_vector))
        
    V_T = eignvalues_matrix

    return V_T
    
                



 
 
def getEigenValues(A):
    
    A_temp = transpose(A,len(A), len(A[0]))
    A  = matrix_multiply_matrix(A, A_temp,len(A), len(A_temp[0]))
    print_matrix(A)
    iterated_a = repeatQR(A)
    eigenvalues = getMatrixDiag(iterated_a)
    print("Eigenvalues:")
    print(eigenvalues)
    return eigenvalues
 
def solve_eignvalues(A):
    c = []
    result = []
  



    for  i in range(len(A[0])):
        c.append(0)

    for i in range(len(A)):
        temp = []
        for x in range(len(A[0])):
            temp.append(0)
        result.append(temp)
        temp = []

    for i in range(len(A)):
        eqs = []

        for  v in range(len(A[0])):
            eqs.append(0)
        flag = False
        index = -1
        for z in range(len(A[0])):
            if round(A[i][z],1) == 1 and (flag == False):
                flag =  True
                index = z
            elif (flag):
                if (A[i][z] != 0):
                    eqs[z] = 0 - A[i][z]

        
        if ( index != -1):
            result[i][index] = eqs
      
            
  
    print_matrix(result)

    vector = []
    for  v in range(len(A[0])):
        vector.append(0)

    for i in range(len(result)):
      
        flag = True
        count = 0

        for x in range(len(result[0])):
  
            if (result[i][x] != None and result[i][x]!= 0):

                for c in range(len(result[i][x])):
                    
                    if (round(result[i][x][c],1) != 0):
                        vector[x] = (result[i][x][c])
                        
    for i in range(len(result[0])):
        count = 0
        for x in range(len(result)):
           
    
            if  isinstance(result[x][i], list) == False and round(result[x][i],1) == 0:
                count += 1
                
        if count == len(result):
            vector[i] = 1



    vector = vector_divide_mag(vector,get_magnitude_vector(vector))
    return vector
                    
def get_transpose_col(A):
    result = []
    for i in A:
        temp = []
        temp.append(i)
        result.append(temp)

    return result


def get_U(A,V_T,S,lambdas): 
   # S_inv = getMatrixInv(S)
    #print(S_inv)
    #V = transpose(V_T, len(V_T), len(V_T[0]))
    #A_V = matrix_multiply_matrix(A, V, len(A),len(V[0]) )
    #A_V_S_INV = matrix_multiply_matrix(A_V, S_inv, len(A_V), len(S_inv[0]))

    result = []
    for i in range(len(lambdas)):
        U = (float)(1.0/lambdas[i])
        U_AT =  matrix_multiply_num(transpose(A, len(A), len(A[0])), U)
    
        V = get_transpose_col(V_T[i])
        print("V:")
        print_matrix(V) 
        print("U_AT")
        print_matrix(U_AT)
        print(len(U_AT))
        print(len(V[0]))
        U_AT_EgnVector = matrix_multiply_matrix(U_AT,V , len(U_AT), len(V[0]) )
        result.append(U_AT_EgnVector)
    result = transpose(result, len(result), len(result[0]))
    print_matrix(result)





    

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
    vectors = getEigenValues(A)
    #A = [[9,4], [9,16]]
    #getSquareRoots(A)
    #print_matrix(A)
    #repeatQR(A)
    lambdas = getSingularValues(vectors)
    
    
    S = getSingularMatrix(A,lambdas)

    print("EigenVectors:")
    V_T = getEigenVectors(A,vectors)
    print_matrix(V_T)
    
    get_U(A, V_T, S, lambdas )
    
    
    
    
    