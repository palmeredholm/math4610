# Matrix Transpose

**Routine Name:** transpose

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the transpose of a given matrix.

**Input:** This routine has one input variable:

* A: Matrix to be transposed.

**Output:** This routine returns a matrix that has been transposed.

**Usage/Example:**

We can implement the following code to transpose a matrix.
```python
A = [[1, 2],
     [3, 4]]
C = transpose(A)
for row in C:
    print(row)
```
Output from the lines above:
```python
[1, 3]
[2, 4]
```
The above result is the transpose of the aforementioned matrix.

**Implementation/Code:** The following is the code for transpose(A)
```python
def transpose(A):
    # Return the transpose of the given matrix A
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
```

**Last Modified:** December/2021

<hr>

[Previous](mat_scalar.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](mat_vec_prod.md)

<hr>
