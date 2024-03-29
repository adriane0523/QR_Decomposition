import random
from Inverse import *

def print_matrix(A):
    print("______________________________\n")
    for i in A:
        print('      ', i)
    print("______________________________\n")

def QR_decomposition(A, m , n ):
    #m: row
    #n: column    
    count = 0

    vector = []
    
    column = 0
    while (column < n ):
        temp = []
        row = 0
        while (row < m):
            temp.append(A[row][column])
            row+=1
        column+=1
        vector.append(temp)
    #print(vector)
  
    Q = []


    q_1 = vector_divide_mag( vector[0], get_magnitude_vector( vector[0] ) )
    Q.append(q_1)
    vector_index = 1
    vector_sum = []
    for i in range(len(vector[0])):
        vector_sum.append(0)
    

    while ( vector_index < n ):
        x = vector_index

        while(x > 0):
          #  print("")
          #  print("Current vector index", x)
          #  print("Current index", n)
            q_dot = vector_multiply_num( Q[x - 1], dot( Q[x - 1], vector[vector_index] ) ) 
          #  print( "DOT:",dot( Q[x - 1], vector[vector_index] ))
         #   print("MULTIPLY:",q_dot)
            vector_sum = vector_add_vector(vector_sum, q_dot)
         #   print("SUM:", vector_sum)
            x = x - 1

        q = vector_subtract_vector( vector[vector_index], vector_sum )
      #  print("SUB:",q )
       
        q_num = vector_divide_mag( q, get_magnitude_vector( q ) )
        Q.append(q_num)
        #print_matrix(Q)
        vector_sum = []
        for i in range(len(vector[0])):
            vector_sum.append(0)
        vector_index = vector_index + 1
        


    row = 0
    column = 0
    
    

    # Q = vector_combine_to_matrix(q_1, q_2)
    #convert vector array to matrix
    Q = transpose(Q, n,m)
#    for i in range(len(Q)):
 #       for j in range(len(Q[0])):
 #           if Q[i][j] <= 0.0005 and Q[i][j]*-1 < 0:
 #               Q[i][j] = 0
    #print("\n\nQ:")
    #print_matrix(Q)
    
    tranpose_Q = transpose(Q, m,n)
    #print_matrix(tranpose_Q)
    m_n = get_new_m_n(tranpose_Q, A)
    
   # R = matrix_multiply_matrix(tranpose_Q, A, len(tranpose_Q), len(A[0]))
    
  

    #print("\n\nR:")
    #print_matrix(R)
    
    #print("\n\nVerification that Q * R = A:")     
    #print_matrix(matrix_multiply_matrix(Q,R,n,m))

    Q_2 = matrix_multiply_matrix(tranpose_Q, Q, len(tranpose_Q), len(Q[0]))
    Q_2 = getMatrixInv(Q_2)
    R = matrix_multiply_matrix(matrix_multiply_matrix(Q_2, tranpose_Q, m , n), A, m, n)

    #for i in range(len(R)):
     #   for j in range(len(R[0])):
     #       if R[i][j] <= 0.0005 and R[i][j] >= -0.0005 :
     #           R[i][j] = 0

    print(R)
    
    QR = []
    QR.append(Q)
    QR.append(R)
    return QR



def vector_add_vector(vector_1, vector_2):
    result = []
    for i in range(len(vector_1)):
         result.append(vector_1[i] + vector_2[i])
    return result


def vector_combine_to_matrix(vector_1, vector_2):
    result = []
    row = []
    count = 0
    for i in vector_1:
        row.append(i)
        row.append(vector_2[count])
        count = count + 1
        result.append(row)
        row = []
    return result

def get_new_m_n(matrix_1, matrix_2):
    
    count = 0
    for i in matrix_1:
        count = count + 1
    
    return [ count, len(matrix_2[0])]

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

def vector_multiply_num(vector_1,num):
    result = []
    for i in vector_1:
        result.append((float)(i * num))
        

    return result

def dot(vector_1, vector_2):
    result = 0
    count = 0
    for i in vector_1:
        result = float(result + (float)(i * vector_2[count]))
        count = count + 1
    return result

def vector_subtract_vector(vector_1, vector_2):
    result = []
    count = 0
    for i in vector_1:
        result.append((float)(i - vector_2[count]))
        count = count + 1

    return result
          

def get_magnitude_vector(vector_1):
    result = 0
    for i in vector_1:
        result = result + (float)(i**2)
    
    return (float)(result**(1/2))

def vector_divide_mag(vector_1, magnitude):
    result = []
    for i in vector_1:
        if (magnitude == 0.0):
            result.append(0.0)
        else:
            result.append((float)(i/magnitude))

    return result




def test_cases(A, ans):
    print_matrix(A)
    result =  True
    for i in range(len(A)):
        if A[i] != ans[i]:
            result = False
    return result

def random_A(m,n):
    result = []
    for i in range(m):
        temp = []
        for x in range(n):
            temp.append(random.randint(0,10))
        result.append(temp)
        
    return result

def matrix_multiply_num(matrix,num):
    result = []
    for i in range(len(matrix)):
        temp = []
        for x in range(len(matrix[0])):
            temp.append((float)(matrix[i][x] * num))
        result.append(temp)
        temp = []
    return result            
        

if __name__ == "__main__":
    #A = [[2,3],[2,4],[1,1]], 
    A = [  [5,4,6,],
        [4,5,6],
        [6,6,8] ] 
            
    #A = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
    #A = [[2, -1, 1], [1, 3, -2], [0, 1, -2]]
    # #####A = [[45, 30, -25], [30, -24, 68], [-25, 68, 80]]
    #A = [[2, 3, 4, 1], [2, 1, 5, 3], [2, 4, 5, 4], [1, 4, 4, 6]]
    #A = [[2, 4, 5], [2, 3, 5], [2, 2, 2], [3, 5, 6], [1, 2, 4]]
    #A = [[6, -7, 2], [4, -5, 2], [1, -1, 1]]

    #x = random_A(1000,3)

    #print_matrix(x)
    QR = QR_decomposition(A,len(A),len(A[0]))
    print("Q:")
    print_matrix(QR[0])
    print("R:")
    print_matrix(QR[1])
