# LU Factorization

**Routine Name:** lu

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine computes the LU factorization of a given matrix. LU factorization is extremely helpful
for many computational problems that often arise.

**Input:** This routine has one input variable:

* A: The coefficient matrix to be decomposed

**Output:** This routine returns a tuple of the decomposed lower and upper triangular matrices of the original coefficient
matrix A.

**Usage/Example:**

The following code implements the LU factorization method on a 5 x 5 diagonally dominant coefficient matrix with random 
entries in the interval [-20,20].
```python
from more_matgen import diag_dom


D = diag_dom(5, -20, 20)
print('Diagonally Dominant Matrix:')
for row in D:
    print(row)
L, U = lu(D)
print(f'L:\n{L}\nU:\n{U}')
```
Output from the lines above:
```python
Diagonally Dominant Matrix:
[8, 8, 0, 0, 0]
[-6, -7, -1, 0, 0]
[-9, 1, 16, 3, -1]
[5, 1, 0, 6, 0]
[2, 1, 1, 0, -4]
L:
[[  1.           0.           0.           0.           0.        ]
 [ -0.75         1.           0.           0.           0.        ]
 [ -1.125      -10.           1.           0.           0.        ]
 [  0.625        4.           0.66666667   1.           0.        ]
 [  0.25         1.           0.33333333  -0.25         1.        ]]
U:
[[ 8.          8.          0.          0.          0.        ]
 [ 0.         -1.         -1.          0.          0.        ]
 [ 0.          0.          6.          3.         -1.        ]
 [ 0.          0.          0.          4.          0.66666667]
 [ 0.          0.          0.          0.         -3.5       ]]
```
As we can see, the routine successfully decomposes the matrix into its lower and upper triangular components.

**Implementation/Code:** The following is the code for lu(A)
```python
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
```
**Last Modified:** November/2021

<hr>

[Previous](solve.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](sc_part_pivot.md)

<hr>
