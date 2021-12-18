# Scalar Multiplication for Vectors

**Routine Name:** vec_scalar

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the scalar multiplication for a scalar and a vector.

**Input:** This routine has two input variables:

* a: Constant scalar.
* x: Vector to be scaled.

**Output:** This routine returns a vector that is scaled by the scalar passed in.

**Usage/Example:**

We can implement the following code to scale a vector.
```python
a = 2
x = [1, 2, 3, 4, 5]
print(vec_scalar(a, 2))
```
Output from the lines above:
```python
[2, 4, 6, 8, 10]
```
The above result is the vector (1, 2, 3, 4, 5) scaled by the scalar 2.

**Implementation/Code:** The following is the code for vec_scalar(a, x)
```python
def vec_scalar(a, x):
    # Return the vector x where each element is scaled by the scalar a
    return [a * x[i] for i in range(len(x))]
```

**Last Modified:** December/2021

<hr>

[Previous](vec_subtract.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](vec_dot_prod.md)

<hr>
