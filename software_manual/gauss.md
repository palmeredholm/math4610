# Gaussian Elimination

**Routine Name:** gauss

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine performs Guassian elimination on an augmented matrix to reduce it to row echelon form.
This routine assumes that the matrix is nonsingular.

**Input:** This routine has two input variables:

* A: Nonsingular coefficient matrix to a system of equations.
* b: b vector in the system of equations.

**Output:** This routine returns a tuple of the coefficient matrix and the b vector after the augmented matrix has been
reduced to row echelon form.

**Usage/Example:**

We can implement the following code to reduce the following square matrix and b vector.
```python
import numpy as np
from mat_gen import square


A = np.asarray(square(5))
b = np.ones(5)
red = gauss(A, b)[0]
sol = gauss(A, b)[1]
print(f'A:\n{A}\nb:\n{b}\nRow echelon form:\n{red}\nb Vector:\n{sol}')
```
Output from the lines above:
```python
A:
[[50 46 28 20 68]
 [92 13 69 41 68]
 [24 12 63 93 22]
 [ 9 58 28  3 34]
 [ 4 46 48 27  7]]
b:
[1. 1. 1. 1. 1.]
Row echelon form:
[[ 50  46  28  20  68]
 [  0 -71  17   4 -57]
 [  0   0  46  82  -1]
 [  0   0   0 -56 -17]
 [  0   0   0   0  -8]]
b Vector:
[ 1.         -2.68        0.53577465 -2.63157379  0.96634109]
```
As we can see, our gauss routine reduces the augmented matrix to row echelon form so that the system can be solved by back
substitution.

**Implementation/Code:** The following is the code for gauss(A, b)
```python
import numpy as np


def gauss(A, b):
    # Copy the matrix that was passed in to reduce and initialize n for loops
    A = np.asarray(A, np.float)
    b = np.asarray(b, np.float)
    n = len(b)
    # Traverse columns 1 to n-1
    for k in range(n - 1):
        for i in range(k + 1, n):
            # Initialize factor variable to lessen computational costs
            factor = A[i, k] / A[k, k]
            # Reduce each element before the pivot to 0 and change the associated value of the b
            # vector
            for j in range(k, n):
                A[i, j] -= factor * A[k, j]
            b[i] -= factor * b[k]
    # Return reduced augmented matrix
    return A, b
```
**Last Modified:** November/2021

<hr>

[Previous](matgen.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](more_matgen.md)

<hr>
