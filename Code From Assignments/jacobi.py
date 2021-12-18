from vec_err import err_2
from solve import solve
from more_matgen import diag_dom
from matrix_ops import mat_vec_prod
import numpy as np


def jacobi(A, b, x0, tol, max_iter):
    # Initialize variables needed for iterating
    n = len(b)
    r = [0 for i in range(len(b))]
    x1 = [0 for i in range(len(x0))]
    error = tol * 10.0
    iters = 0
    # Start iterating
    while error > tol and max_iter > iters:
        # Calculate the residual
        for i in range(n):
            r[i] = b[i]
            for j in range(n):
                r[i] += A[i][j] * x0[j]
        # Update the approximating vector
        for i in range(n):
            x1[i] = x0[i] - (r[i] / A[i][i])
        # Calculate l-2 error
        error = err_2(x0, x1)
        iters += 1
        # Create new x0 vector to continue iterating
        for i in range(n):
            x0[i] = x1[i]
    # Flip the sign
    x1 = [-1*x1[i] for i in range(len(x1))]
    # Return approximated solution
    return x1


A = diag_dom(100)
x = [1 for i in range(100)]
b = mat_vec_prod(A, x)
sol_1 = solve(A, b)
print(sol_1)