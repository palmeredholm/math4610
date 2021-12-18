# 2-Matrix Norm

**Routine Name:** norm_2

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine computes the 2-norm of a matrix which is also known as the spectral norm. This routine
simply computes the largest singular value of a matrix.

**Input:** This routine has one input variable.

* A: Matrix for which to compute the infinity-norm.

**Output:** This routine returns a scalar that is the largest singular value of the matrix.

**Usage/Example:**

The following code will compute the 2-norm of a matrix.
```python
A = [[1, -2],
     [3, -4]]
print(norm_2(A))
```
Output from the lines above:
```python
5.464985704218306
```
The above value is the largest singular value of the above matrix.

**Implementation/Code:** The following is the code for norm_2(A)
```python
from power import power
from matrix_ops import transpose, mat_prod


def norm_2(A):
    A = mat_prod(transpose(A), A)
    return (power(A, [50 for i in range(len(A))], 50, 0.0001, 1000))**0.5
```
**Last Modified:** December/2021

<hr>

[Previous](mat_norm_linf.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](parallel.md)

<hr>
