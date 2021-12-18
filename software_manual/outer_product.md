# Outer Product

**Routine Name:** out_prod

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the outer product of two conformable vectors.

**Input:** This routine has two input variables:

* x: Vector to the left.
* y: Vector to the right.

**Output:** This routine returns a matrix that is the outer product of two conformable vectors.

**Usage/Example:**

We can implement the following code to compute the outer product.
```python
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
A = out_prod(x, y)
for row in A:
    print(row)
```
Output from the lines above:
```python
[1.0, 2.0, 3.0, 4.0, 5.0]
[2.0, 4.0, 6.0, 8.0, 10.0]
[3.0, 6.0, 9.0, 12.0, 15.0]
[4.0, 8.0, 12.0, 16.0, 20.0]
[5.0, 10.0, 15.0, 20.0, 25.0]
```
The above result is the outer product of the vectors (1, 2, 3, 4, 5) and (1, 2, 3, 4, 5).

**Implementation/Code:** The following is the code for out_prod(x, y)
```python
def out_prod(x, y):
    # Check to see if vectors are conformable
    if len(x) != len(y):
        raise Exception('Non-conformable arrays')
    # Initialize matrix to fill with the elements of the outer product of x and y
    out = [[0 for i in range(len(x))] for j in range(len(x))]
    # Traverse the elements of each vector and create the respective element of the outer product
    for i in range(len(x)):
        for j in range(len(x)):
            out[i][j] = float(x[i]) * float(y[j])
    # Return outer product matrix
    return out
```

**Last Modified:** December/2021

<hr>

[Previous](vec_dot_prod.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](vec_mag_l1.md)

<hr>
