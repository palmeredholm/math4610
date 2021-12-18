# Vector Dot Product

**Routine Name:** dot_prod

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the dot product of two conformable vectors.

**Input:** This routine has two input variables:

* x: Vector to the left of the dot.
* y: Vector to the right of the dot.

**Output:** This routine returns a scalar that is the dot product of two conformable vectors.

**Usage/Example:**

We can implement the following code to compute the dot product.
```python
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
print(dot_prod(x, y))
```
Output from the lines above:
```python
55.0
```
The above result is the dot product of the vectors (1, 2, 3, 4, 5) and (1, 2, 3, 4, 5).

**Implementation/Code:** The following is the code for dot_prod(x, y)
```python
def dot_prod(x, y):
    # Check to see if vectors are conformable
    if len(x) != len(y):
        raise Exception('Non-conformable arrays')
    # Initialize a sum variable
    dot = 0
    # Traverse each element in either array and sum the product of the respective elements
    for i in range(len(x)):
        dot += float(x[i]) * float(y[i])
    # Return the dot product of the two vectors
    return dot
```

**Last Modified:** December/2021

<hr>

[Previous](vec_scalar.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](outer_product.md)

<hr>
