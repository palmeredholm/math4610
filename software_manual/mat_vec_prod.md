# Dot Product of a Matrix and a Vector

**Routine Name:** mat_vec_prod

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the dot product of a conformable matrix and vector.

**Input:** This routine has two input variables:

* A: Matrix to the left of the dot.
* x: Vector to the right of the dot.

**Output:** This routine returns a vector that is the result of the dot product of a conformable matrix and vector.

**Usage/Example:**

We can implement the following code to take the dot product of a matrix and a vector.
```python
A = [[1, 2],
     [3, 4]]
x = [1, 2]
b = mat_vec_prod(A, x)
print(b)
```
Output from the lines above:
```python
[5.0, 11.0]
```
The above result is the dot product of the listed matrix and vector.

**Implementation/Code:** The following is the code for mat_vec_prod(A, x)
```python
def mat_vec_prod(A, x):
    # Check to see if this matrix and vector are conformable
    if (not isinstance(A[0], list)) or (len(A[0]) != len(x)) or (len(A) <= 1) or (isinstance(x[0], list)):
        raise Exception('Non-conformable')
    # Initialize empty resultant vector
    B = [0 for i in range(len(A))]
    # Sum the respective products
    for i in range(len(A)):
        el = 0
        for j in range(len(x)):
            el += float(A[i][j]) * float(x[j])
        B[i] = el
    # Return resultant vector
    return B
```

**Last Modified:** December/2021

<hr>

[Previous](mat_transpose.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](mat_prod.md)

<hr>
