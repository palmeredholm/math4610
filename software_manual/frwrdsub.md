# Forward Substitution

**Routine Name:** frwrdsub

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the solution to a system of equations once that system has already
been reduced to lower triangular. This routine uses forward substitution to solve for the unkowns of the system. This routine
assumes that the matrix passed in is already in lower triangular.

**Input:** There are two input variables in this routine:

* A: Coefficient matrix of a system of equations in lower triangular form.
* b: b vector in Ax=b

**Output:** This routine returns the vector x which is the solution to the system of equations.

**Usage/Example:**

If we have a matrix A in lower triangular form and a b vector, we can implement the following code to perform forward
substitution and solve the system of equations.
```python
import numpy as np


A = np.array([[1, 0, 0, 0],
              [2, 3, 0, 0],
              [3, 4, 5, 0],
              [4, 5, 6, 7]], np.float)
b = np.ones(4)
x = frwrdsub(A, b)
print(x)
```
Output from the lines above:
```python
[ 1.         -0.33333333 -0.13333333 -0.07619048]
```
Given the coefficient matrix A (which is just the tranpose of the matrix from the example in the back substitution routine)
and the vector of ones as the b vector, the output shown above is the solution to the system of equations. 

**Implementation/Code:** The following is the code for frwrdsub(A, b)
```python
import numpy as np


def frwrdsub(A, b):
    # Initialize vector of unkowns and variable of the length of the solution vector for our loops
    x = np.empty_like(b)
    n = len(b)
    # Compute the first unknown of the system
    x[0] = b[0] / A[0, 0]
    # Traverse the matrix
    for i in range(1, n):
        # Initialize sum variable to simplify later substitutions
        sum = b[i]
        # Traverse each element of the current row to find the value of the associated unknown
        for j in range(i):
            sum -= A[i, j] * x[j]
        x[i] = sum / A[i, i]
        # Return the solution to the system
    return x
```
**Last Modified:** November/2021

<hr>

[Previous](backsub.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](matgen.md)

<hr>
