# Vector Difference 2-Norm

**Routine Name:** err_2

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the error between two vectors using the 2-norm.

**Input:** This routine has two input variables:

* x: Vector estimating the true vector y.
* y: Vector to be estimated.

**Output:** This routine returns a scalar that gives a measurement of the error in approximation using the 2-norm.

**Usage/Example:**

We can implement the following code to compute the 2-norm error.
```python
x = [1, -2, 3, -4, 5]
y = [1, 2, 3, 4, 5]
print(err_2(x, y))
```
Output from the lines above:
```python
8.94427190999916
```
The above result is the 2-norm error in approximating the vector (1, 2, 3, 4, 5) with the vector (1, -2, 3, -4, 5).

**Implementation/Code:** The following is the code for err_2(x, y).
```python
from vectors import vec_subtract
from norms import norm_2


def err_2(x, y):
    # Check to see if vectors are conformable
    if len(x) != len(y):
        raise Exception('Non-conformable arrays')
    # Return the l2 error between x and y
    return norm_2(vec_subtract(x, y))
```
**Last Modified:** December/2021

<hr>

[Previous](vec_err_l1.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](vec_err_linf.md)

<hr>
