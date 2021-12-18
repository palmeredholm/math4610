# Vector Addition

**Routine Name:** vec_add

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the vector addition of two conformable vectors.

**Input:** This routine has two input variables:

* x: First vector to be added.
* y: Second vector to be added.

**Output:** This routine returns a vector that is the addition of two vectors passed in.

**Usage/Example:**

We can implement the following code to add two conformable vectors together.
```python
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
print(vec_add(x, y))
```
Output from the lines above:
```python
[2, 4, 6, 8, 10]
```
The above result is the addition of the vectors (1, 2, 3, 4, 5) and (1, 2, 3, 4, 5).

**Implementation/Code:** The following is the code for vec_add(x, y)
```python
def vec_add(x, y):
    # Check to see if vectors are conformable
    if len(x) != len(y):
        raise Exception('Non-conformable arrays')
    # Return the element-wise addition of the two vectors
    return [x[i] + y[i] for i in range(len(x))]
```

**Last Modified:** December/2021

<hr>

[Previous](sc_part_pivot.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](vec_subtract.md)

<hr>
