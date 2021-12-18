# Vector 2-Norm

**Routine Name:** norm_2

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the 2-norm of a vector. The 1-norm is an alternative way of measuring
the magnitude of a vector.

**Input:** This routine has one input variable:

* x: Vector for which to compute the 2-norm.

**Output:** This routine returns a scalar that is the square root of the sum of the squares of the entries in the vector.

**Usage/Example:**

We can implement the following code to compute the 2-norm of a vector.
```python
x = [1, -2, 3, -4, 5]
print(norm_2(x))
```
Output from the lines above:
```python
7.416198487095663
```
The above result is the 2-norm of the vector (1, -2, 3, -4, 5).

**Implementation/Code:** The following is the code for norm_2(x).
```python
def norm_2(x):
    # Initialize sum variable
    norm = 0
    # Traverse the vector and sum the squares
    for i in range(len(x)):
        norm += float(x[i]) * float(x[i])
    # Return the square of the sum of the squares (i.e., the l2 norm)
    return norm ** 0.5
```
**Last Modified:** December/2021

<hr>

[Previous](vec_mag_l1.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](vec_mag_linf.md)

<hr>
