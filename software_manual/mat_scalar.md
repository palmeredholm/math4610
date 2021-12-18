# Scalar Multiplication for Matrices

**Routine Name:** mat_scalar

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the scalar multiplication for a scalar and a matrix.

**Input:** This routine has two input variables:

* a: Constant scalar.
* A: Matrix to be scaled.

**Output:** This routine returns a matrix that is scaled by the scalar passed in.

**Usage/Example:**

We can implement the following code to scale a matrix.
```python
A = [[1, 2],
     [3, 4]]
C = mat_scalar(2, A)
for row in C:
    print(row)
```
Output from the lines above:
```python
[2, 4]
[6, 8]
```
The above result is the aforementioned matrix scaled by the scalar 2.

**Implementation/Code:** The following is the code for mat_scalar(a, A)
```python
def mat_scalar(a, A):
    return [[a * A[i][j] for j in range(len(A[i]))] for i in range(len(A))]
```

**Last Modified:** December/2021

<hr>

[Previous](mat_subtract.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](mat_transpose.md)

<hr>
