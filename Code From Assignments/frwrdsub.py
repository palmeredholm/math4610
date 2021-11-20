import numpy as np


def frwrdsub(A, b):
    # Initialize vector of unkowns and variable of the length of the solution vector for our loops
    x = np.empty_like(b)
    n = len(b)
    # Compute the first unknown of the system
    x[0] = b[0] / A[0, 0]
    # Traverse the matrix
    for i in range(1, n):
        # Initialize sum variable to simplify later substitutions
        sum = b[i]
        # Traverse each element of the current row to find the value of the associated unknown
        for j in range(i):
            sum -= A[i, j] * x[j]
        x[i] = sum / A[i, i]
        # Return the solution to the system
    return x


def transpose(A):
    # Transpose the given matrix A
    return [[A[j, i] for j in range(len(A))] for i in range(len(A[0]))]
