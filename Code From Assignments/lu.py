import numpy as np


def lu(A):
    # Initialize matrices for the upper and lower decompositions of A
    U = np.asarray(A, np.float)
    L = np.identity(len(U[0]), np.float)
    n = len(U[0])
    # Perform Gaussian Elimination
    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = U[i, k] / U[k, k]
            for j in range(k, n):
                U[i, j] -= factor * U[k, j]
            # Create L matrix
            L[i][k] = factor
    return L, U
