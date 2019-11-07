



def print_matrix(A):
    print("__________________\n")
    for i in A:
        print(i)
    print("_________________\n")

def QR_decomposition(A, m , n ):
    #m: row
    #n: column

    if (m < n):
        print("m is less than n, can't do QR decomp")
    else: 

        
        count = 0

        vector = []
        
        column = 0
        while (column < m ):
            temp = []
            row = 0
            while (row < n):
                temp.append(A[row][column])
                row+=1
            column+=1
            vector.append(temp)
        print(vector)
        
        #vector_1 = [ A[0][0], A[1][0], A[2][0] ]
        #vector_2 = [ A[0][1], A[1][1], A[2][1] ]
        vector_1 = vector[0]
        
        Q = []


        q_1 = vector_divide_mag( vector[0], get_magnitude_vector( vector[0] ) )
        Q.append(q_1)
        vector_index = 1
        vector_sum = []
        for i in range(len(vector[0])):
            vector_sum.append(0)
        

        while ( vector_index < m ):
            x = vector_index
    
            while(x > 0):
                print("")
                print("Current vector index", x)
                print("Current index", n)
                q_dot = vector_multiply_num( Q[x - 1], dot( Q[x - 1], vector[vector_index] ) ) 
                print( "DOT:",dot( Q[x - 1], vector[vector_index] ))
                print("MULTIPLY:",q_dot)
                vector_sum = vector_add_vector(vector_sum, q_dot)
                print("SUM:", vector_sum)
                x = x - 1

            q = vector_subtract_vector( vector[vector_index], vector_sum )
            print("SUB:",q )
            q_num = vector_divide_mag( q, get_magnitude_vector( q ) )
            Q.append(q_num)
            print_matrix(Q)
            vector_sum = []
            for i in range(len(vector[0])):
                vector_sum.append(0)
            vector_index = vector_index + 1
            


        row = 0
        column = 0
        
        

       # Q = vector_combine_to_matrix(q_1, q_2)
        #convert vector array to matrix
        Q = transpose(Q, m,n)
        print("\n\nQ:")
        print_matrix(Q)
        
        tranpose_Q = transpose(Q, n,m)
        #print_matrix(tranpose_Q)
        m_n = get_new_m_n(tranpose_Q, A)
        
        R = matrix_multiply_matrix(tranpose_Q, A, m_n[0], m_n[1])

        print("\n\nR:")
        print_matrix(R)

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
    
        # iterating by coloum by B  
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
        result.append((float)(i/magnitude))

    return result
        

if __name__ == "__main__":
   # A = [[2,3],[2,4],[1,1]]
    A = [[2,3, 1], [3,5,1]]
    print_matrix(A)
    QR_decomposition(A,3,2)