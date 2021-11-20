# Back Substitution

**Routine Name:** backsub

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the solution to a system of equations once that system has already
been reduced to upper triangular. This routine uses back substitution to solve for the unkowns of the system. This routine
assumes that the matrix passed in is already in upper triangular.

**Input:** There are two input variables in this routine:

* A: Coefficient matrix to a system of equations in upper triangular form.
* b: b vector in Ax=b

**Output:** This routine returns the vector x which is the solution to the system of equations.

**Usage/Example:**

If we have a matrix A in upper triangular form and a b vector, we can implement the following code to perform back substitution
and solve the system of equations.
```python
import numpy as np


A = np.array([[1, 2, 3, 4],
              [0, 3, 4, 5],
              [0, 0, 5, 6],
              [0, 0, 0, 7]], np.float)
b = np.ones(4)
x = backsub(A, b)
print(x)
```
Output from the lines above:
```python
[0.22857143 0.05714286 0.02857143 0.14285714]
```
Given the coefficient matrix A and the vector of ones as the b vector, the output shown above is the solution to the system
of equations. 

**Implementation/Code:** The following is the code for backsub(A, b)
```python
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
        # Traverse each element in the current row and compute the value of the unkown associated
        # with that row
        for j in range(i + 1, n):
            sum -= A[i, j] * x[j]
        x[i] = sum / A[i, i]
        # Return the solution to the system
    return x
```
**Last Modified:** November/2021

<hr>

[Previous](roots.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](frwrdsub.md)

<hr>
