# Matrix Subtraction

**Routine Name:** mat_subtract

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the matrix subtraction of two conformable matrices.

**Input:** This routine has two input variables:

* x: First matrix to be subtracted.
* y: Second matrix to be subtracted.

**Output:** This routine returns a matrix that is the subtraction of two matrices passed in.

**Usage/Example:**

We can implement the following code to subtract two conformable matrices.
```python
A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
C = mat_subtract(A, B)
for row in C:
    print(row)
```
Output from the lines above:
```python
[-4, -4]
[-4, -4]
```
The above result is the subtraction of the matrices listed.

**Implementation/Code:** The following is the code for mat_subtract(A, B)
```python
def mat_subtract(A, B):
    # Check to see if matrices are conformable
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise Exception('Matrices are non-conformable')
    # Create matrix for addition of values
    C = [[0 for i in range(len(A))] for j in range(len(A))]
    # Traverse the two matrices and update the C matrix with the subtraction of the elements
    for i in range(len(C)):
        for j in range(len(C)):
            C[i][j] = A[i][j] - B[i][j]
    # Return the matrix subtraction of A and B
    return C
```

**Last Modified:** December/2021

<hr>

[Previous](mat_add.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](mat_scalar.md)

<hr>
