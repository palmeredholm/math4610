# Matrix Dot Product

**Routine Name:** mat_prod

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the dot product of two conformable, rectangular matrices.

**Input:** This routine has two input variables:

* A: Matrix to the left of the dot.
* B: Matrix to the right of the dot.

**Output:** This routine returns a matrix that is the result of the dot product of two conformable, rectangular matrices.

**Usage/Example:**

We can implement the following code to take the dot product of two rectangular matrices.
```python
A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
C = mat_prod(A, B)
for row in C:
    print(row)
```
Output from the lines above:
```python
[19.0, 22.0]
[43.0, 50.0]
```
The above result is the dot product of the listed matrices.

**Implementation/Code:** The following is the code for mat_prod(A, B)
```python
from vectors import dot_prod


def mat_prod(A, B):
    # Check to see that the matrices are conformable
    if (not isinstance(A[0], list)) or (len(A[0]) != len(B)) or (not isinstance(B[0], list)):
        raise Exception('Non-conformable')
    # Initialize empty matrix for resultant dot product
    C = [[0 for i in range(len(A))] for j in range(len(A))]
    # Traverse both matrices and append resulting dot product to C
    for i in range(len(A)):
        for j in range(len(A)):
            C[i][j] = dot_prod(A[i], [row[j] for row in B])
    # Return resultant matrix
    return C
```

**Last Modified:** December/2021

<hr>

[Previous](mat_vec_prod.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](jacobi.md)

<hr>
