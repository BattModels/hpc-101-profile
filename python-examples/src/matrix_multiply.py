import numpy as np

def matrix_multiply_naive(A, B):
    n, m = A.shape
    m2, p = B.shape
    C = np.zeros((n, p))
    for i in range(n):         
        for j in range(p):      
            for k in range(m):  
                C[i,j] += A[i,k] * B[k,j]
    return C