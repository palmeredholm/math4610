# Vector Infinity-Norm

**Routine Name:** norm_inf

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the infinity-norm of a vector. The infinity-norm is an alternative way of measuring
the magnitude of a vector.

**Input:** This routine has one input variable:

* x: Vector for which to compute the infinity-norm.

**Output:** This routine returns a scalar that is the largest absolute value entry in the vector.

**Usage/Example:**

We can implement the following code to compute the infinity-norm of a vector.
```python
x = [1, -2, 3, -4, 5]
print(norm_inf(x))
```
Output from the lines above:
```python
5
```
The above result is the infinity-norm of the vector (1, -2, 3, -4, 5).

**Implementation/Code:** The following is the code for norm_inf(x).
```python
def norm_inf(x):
    # Return the largest absolute value element (i.e., the l infinity norm)
    return max(x, key=abs)
```
**Last Modified:** December/2021

<hr>

[Previous](vec_mag_l2.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](vec_err_l1.md)

<hr>
