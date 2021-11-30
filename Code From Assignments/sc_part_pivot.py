import numpy as np


def sc_part_pivot(A):
    # Initialize needed matrices and arrays
    A = np.asarray(A, np.float)
    B = np.zeros((len(A[0]), len(A[0])), np.float)
    n = len(A[0])
    s = np.copy(A[0])
    indmap = [1 for i in range(n)]
    # Fill indmap and compute scales
    for i in range(n):
        indmap[i] = i
        smax = 0
        for j in range(n):
            smax = max(smax, abs(A[i, j]))
        s[i] = smax
    for k in range(n-1):
        rmax = 0
        # Find largest elements in each row and update indmap accordingly
        for i in range(k, n):
            r = abs(A[indmap[i], k] / s[indmap[i]])
            if r > rmax:
                rmax, j = r, i
        indmap[j], indmap[k] = indmap[k], indmap[j]
        # Perform LU factorization
        for i in range(k+1, n):
            xmult = A[indmap[i], k] / A[indmap[k], k]
            for j in range(k, n):
                A[indmap[i], j] -= xmult * A[indmap[k], j]
            B[indmap[i], k] = xmult
    # Arrange L and U matrices according to indmap
    U = np.empty_like(A, np.float)
    L = np.empty_like(A, np.float)
    for j in range(n):
        U[j] = A[indmap[j]]
        L[j] = B[indmap[j]]
        L[j, j] = 1.0
    return L, U
