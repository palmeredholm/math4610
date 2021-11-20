import numpy as np


def gauss(A, b):
    # Copy the matrix that was passed in to reduce and initialize n for loops
    A = np.copy(A)
    n = len(b)
    # Traverse columns 1 to n-1
    for k in range(n - 1):
        for i in range(k + 1, n):
            # Initialize factor variable to lessen computational costs
            factor = A[i, k] / A[k, k]
            # Reduce each element before the pivot to 0 and change the associated value of the b vector
            for j in range(k, n):
                A[i, j] -= factor * A[k, j]
            b[i] -= factor * b[k]
    # Return reduced augmented matrix
    return A, b
