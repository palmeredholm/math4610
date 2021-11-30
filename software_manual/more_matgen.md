# More Matrix Generation

**Routine Name:** diag_dom, hilbert

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** These two routines create a random diagonally dominant matrix and a Hilbert matrix respectively.
The size of both is determined by the value passed in. The nonzero elements of the diagonally dominant matrix are according
to the interval that is passed in.

**Input:** Both routines share only one input:

* n: Dimension of the matrix (i.e., n x n).

Only the diagonally dominant routine has a random component, thus only it has the following two inputs:

* a: Lower bound of the interval for random integers (default is a=-10). 
* b: Upper bound of the interval for random integers (default is b=10).

**Output:** These routines both return square matrices. The hilbert routine returns an n x n Hilbert matrix. The diag_dom
routine returns a diagonally dominant matrix of size n x n with random elements in the interval [a,b].

**Usage/Example:**

We can implement the following code to generate a 4 x 4 diagonally dominant and Hilbert matrix respectively with random
integers in the interval [-10,10] for the diagonally dominant matrix.
```python
import numpy as np


D = np.asarray(diag_dom(4), np.float)
H = np.asarray(hilbert(4), np.float)
print(f'Diagonally Dominant:\n{D}\nHilbert:\n{H}')
```
Output from the lines above:
```python
Diagonally Dominant:
[[10. -5.  4. -1.]
 [ 4. -5.  0. -1.]
 [ 1. -1. -4.  0.]
 [ 0.  6.  1.  9.]]
Hilbert:
[[1.         0.5        0.33333333 0.25      ]
 [0.5        0.33333333 0.25       0.2       ]
 [0.33333333 0.25       0.2        0.16666667]
 [0.25       0.2        0.16666667 0.14285714]]
```
As can be seen, both matrices satisfy their respective definitions.

**Implementation/Code:** The following is the code for diag_dom(n, a=-10, b=10) and hilbert(n)
```python
import random


def diag_dom(n, a=-10, b=10):
    A = []
    for i in range(n):
        A.append([0 for row in range(n)])
    for j in range(n):
        A[j][j] = random.randint(a, b)
    for k in range(n):
        for l in range(n):
            if k == l:
                continue
            else:
                comp = abs(A[k][k]) - abs(abs(A[k][k]) - sum(abs(el) for el in A[k]))
                A[k][l] = random.randint(-comp, comp)
    return A


def hilbert(n):
    H = []
    for i in range(n):
        H.append([(1/(i + j + 1)) for j in range(n)])
    return H
```
**Last Modified:** November/2021

<hr>

[Previous](gauss.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](solve.md)

<hr>
