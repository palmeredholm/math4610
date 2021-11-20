import numpy as np


def backsub(A, b):
    # Initialize vector for unkowns
    x = np.empty_like(b)
    # Compute length of b for loops
    n = len(b)
    # Initialize m for more concise code
    m = n - 1
    # Compute last element of the x vector
    x[m] = b[m] / A[m, m]
    # Traverse matrix backwards
    for i in range(m - 1, -1, -1):
        # Initialize sum variable to facilitate later computations
        sum = b[i]
        # Traverse each element in the current row and compute the value of the unkown associated with that row
        for j in range(i + 1, n):
            sum -= A[i, j] * x[j]
        x[i] = sum / A[i, i]
        # Return the solution to the system
    return x


def upr_trng(n):
    # Initialize n x n matrix of zeros
    A = np.zeros((n, n))
    # Traverse the matrix to change the values of the upper triangular portion to satisfy the piecewise definition
    for i in range(n):
        for j in range(i, n):
            A[i, j] = (i + 1) + (j + 1) - 1
    # Return the matrix
    return A
