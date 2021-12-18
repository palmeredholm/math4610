# Vector Subtraction

**Routine Name:** vec_subtract

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the vector subtraction of two conformable vectors.

**Input:** This routine has two input variables:

* x: First vector to be subtracted.
* y: Second vector to be subtracted.

**Output:** This routine returns a vector that is the subtraction of two vectors passed in.

**Usage/Example:**

We can implement the following code to subtract two conformable vectors.
```python
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
print(vec_subtract(x, y))
```
Output from the lines above:
```python
[0, 0, 0, 0, 0]
```
The above result is the subtraction of the vectors (1, 2, 3, 4, 5) and (1, 2, 3, 4, 5).

**Implementation/Code:** The following is the code for vec_subtract(x, y)
```python
def vec_subtract(x, y):
    # Check to see if vectors are conformable
    if len(x) != len(y):
        raise Exception('Non-conformable arrays')
    # Return the element-wise subtraction of the two vectors
    return [x[i] - y[i] for i in range(len(x))]
```

**Last Modified:** December/2021

<hr>

[Previous](vec_add.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](vec_scalar.md)

<hr>
