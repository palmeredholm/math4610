# Vector Difference 1-Norm

**Routine Name:** err_1

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the error between two vectors using the 1-norm.

**Input:** This routine has two input variables:

* x: Vector estimating the true vector y.
* y: Vector to be estimated.

**Output:** This routine returns a scalar that gives a measurement of the error in approximation using the 1-norm.

**Usage/Example:**

We can implement the following code to compute the 1-norm error.
```python
x = [1, -2, 3, -4, 5]
y = [1, 2, 3, 4, 5]
print(err_1(x, y))
```
Output from the lines above:
```python
12
```
The above result is the 1-norm error in approximating the vector (1, 2, 3, 4, 5) with the vector (1, -2, 3, -4, 5).

**Implementation/Code:** The following is the code for err_1(x, y).
```python
from vectors import vec_subtract
from norms import norm_1


def err_1(x, y):
    # Check to see if vectors are conformable
    if len(x) != len(y):
        raise Exception('Non-conformable arrays')
    # Return the l1 error between x and y
    return norm_1(vec_subtract(x, y))
```
**Last Modified:** December/2021

<hr>

[Previous](vec_mag_linf.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](vec_mag_l2.md)

<hr>
