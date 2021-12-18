# 1-Matrix Norm

**Routine Name:** norm_1

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine computes the 1-norm of a matrix which is simply the largest absolute value column
sum of a matrix.

**Input:** This routine has one input variable.

* A: Matrix for which to compute the 1-norm.

**Output:** This routine returns a scalar that is the largest absolute value column sum of the matrix.

**Usage/Example:**

The following code will compute the 1-norm of a matrix.
```python
A = [[1, -2],
     [3, -4]]
print(norm_1(A))
```
Output from the lines above:
```python
6
```
The absolute value sum of the second column is the largest absolute value column sum of the matrix; therefore, that is what
this routine returned.

**Implementation/Code:** The following is the code for norm_1(A)
```python
def norm_1(A):
    col_sum = sum(abs(el) for el in [col[0] for col in A])
    for i in range(1, len(A)):
        temp_sum = sum(abs(el) for el in [col[i] for col in A])
        if temp_sum > col_sum:
            col_sum = temp_sum
    return col_sum
```
**Last Modified:** December/2021

<hr>

[Previous](inv_power.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](mat_norm_linf.md)

<hr>
