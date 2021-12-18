# Vector 1-Norm

**Routine Name:** norm_1

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the 1-norm of a vector. The 1-norm is an alternative way of measuring
the magnitude of a vector.

**Input:** This routine has one input variable:

* x: Vector for which to compute the 1-norm.

**Output:** This routine returns a scalar that is the sum of the absolute values of the entries in the vector.

**Usage/Example:**

We can implement the following code to compute the 1-norm of a vector.
```python
x = [1, -2, 3, -4, 5]
print(norm_1(x))
```
Output from the lines above:
```python
15
```
The above result is the 1-norm of the vector (1, -2, 3, -4, 5).

**Implementation/Code:** The following is the code for norm_1(x).
```python
def norm_1(x):
    # Initialize sum variable
    norm = 0
    # Traverse the vector and sum the absolute values
    for i in range(len(x)):
        norm += abs(x[i])
    # Return l1 norm
    return norm
```
**Last Modified:** December/2021

<hr>

[Previous](outer_product.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](vec_mag_l2.md)

<hr>
