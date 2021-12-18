# Matrix Addition

**Routine Name:** mat_add

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the matrix addition of two conformable matrices.

**Input:** This routine has two input variables:

* A: First matrix to be added.
* B: Second matrix to be added.

**Output:** This routine returns a matrix that is the addition of two matrices passed in.

**Usage/Example:**

We can implement the following code to add two conformable matrices together.
```python
A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
C = mat_add(A, B)
for row in C:
    print(row)
```
Output from the lines above:
```python
[6, 8]
[10, 12]
```
The above result is the addition of the 2X2 matrices listed.

**Implementation/Code:** The following is the code for mat_add(A, B)
```python
def mat_add(A, B):
    # Check to see if matrices are conformable
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise Exception('Matrices are non-conformable')
    # Create matrix for addition of values
    C = [[0 for i in range(len(A))] for j in range(len(A))]
    # Traverse the two matrices and update the C matrix with the sum of the elements
    for i in range(len(C)):
        for j in range(len(C)):
            C[i][j] = A[i][j] + B[i][j]
    # Return the matrix addition of A and B
    return C
```

**Last Modified:** December/2021

<hr>

[Previous](vec_err_linf.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](mat_subtract.md)

<hr>
