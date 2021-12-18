# Infinity-Matrix Norm

**Routine Name:** norm_inf

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine computes the infinity-norm of a matrix which is simply the largest absolute value
row sum of a matrix.

**Input:** This routine has one input variable.

* A: Matrix for which to compute the infinity-norm.

**Output:** This routine returns a scalar that is the largest absolute value row sum of the matrix.

**Usage/Example:**

The following code will compute the infinity-norm of a matrix.
```python
A = [[1, -2],
     [3, -4]]
print(norm_inf(A))
```
Output from the lines above:
```python
7
```
The absolute value sum of the second row is the largest absolute value row sum of the matrix; therefore, that is what
this routine returned.

**Implementation/Code:** The following is the code for norm_inf(A)
```python
def norm_inf(A):
    row_sum = sum(abs(el) for el in A[0])
    for i in range(1, len(A)):
        temp_sum = sum(abs(el) for el in A[i])
        if temp_sum > row_sum:
            row_sum = temp_sum
    return row_sum
```
**Last Modified:** December/2021

<hr>

[Previous](mat_norm_l1.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](mat_norm_l2.md)

<hr>
