# Scaled Partial Pivoting

**Routine Name:** sc_part_pivot

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine also computes the LU factorization of a given matrix. However, this routine utilizes
scaled partial pivoting to deal with problems that are not very well-conditioned.

**Input:** This routine has one input variable:

* A: The coefficient matrix to be decomposed

**Output:** This routine returns a tuple of the decomposed lower and upper triangular matrices of the original coefficient
matrix A using scaled partial pivoting.

**Usage/Example:**

We can implement the following code to use scaled partial pivoting on the same diagonally dominant matrix we used in the
LU factorization entry.
```python
A = [[8, 8, 0, 0, 0],
     [-6, -7, -1, 0, 0],
     [-9, 1, 16, 3, -1],
     [5, 1, 0, 6, 0],
     [2, 1, 1, 0, -4]]
L, U = sc_part_pivot(A)
print(f'L:\n{L}\nU:\n{U}')
```
Output from the lines above:
```
L:
[[ 1.          0.          0.          0.          0.        ]
 [ 0.625       1.          0.          0.          0.        ]
 [-1.125      -2.5         1.          0.          0.        ]
 [ 0.25        0.25        0.0625      1.          0.        ]
 [-0.75        0.25       -0.0625      0.14285714  1.        ]]
U:
[[ 8.      8.      0.      0.      0.    ]
 [ 0.     -4.      0.      6.      0.    ]
 [ 0.      0.     16.     18.     -1.    ]
 [ 0.      0.      0.     -2.625  -3.9375]
 [ 0.      0.      0.      0.      0.5   ]]
```
Notice how the decomposed matrices are different from what we got using traditional, straight-forward pivoting.

**Implementation/Code:** The following is the code for sc_part_pivot(A)
```python
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
```
**Last Modified:** November/2021

<hr>

[Previous](lu.md)
| [Table of Contents](toc/manual_toc.md)
| [Next]()

<hr>
