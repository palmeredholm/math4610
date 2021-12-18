# Vector Difference Infinity-Norm

**Routine Name:** err_inf

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the error between two vectors using the infinity-norm.

**Input:** This routine has two input variables:

* x: Vector estimating the true vector y.
* y: Vector to be estimated.

**Output:** This routine returns a scalar that gives a measurement of the error in approximation using the infinity-norm.

**Usage/Example:**

We can implement the following code to compute the infinity-norm error.
```python
x = [1, -2, 3, -4, 5]
y = [1, 2, 3, 4, 5]
print(err_inf(x, y))
```
Output from the lines above:
```python
-8
```
The above result is the infinity-norm error in approximating the vector (1, 2, 3, 4, 5) with the vector (1, -2, 3, -4, 5).

**Implementation/Code:** The following is the code for err_inf(x, y).
```python
from vectors import vec_subtract
from norms import norm_inf


def err_inf(x, y):
    # Check to see if vectors are conformable
    if len(x) != len(y):
        raise Exception('Non-conformable arrays')
    # Return the l infinity error between x and y
    return norm_inf(vec_subtract(x, y))
```
**Last Modified:** December/2021

<hr>

[Previous](vec_err_l2.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](mat_add.md)

<hr>
