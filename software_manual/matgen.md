# Random Matrix Generation

**Routine Name:** square, upr_trng, lwr_trng, diag

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** These four routines are all very similar to each other. Each one creates a square matrix with specified
random integers for each element, the upper triangular portion, the lower triangular portion, or the diagonal elements.

**Input:** Each routine has the same three inputs:

* n: Dimension of the matrix (i.e., n x n).
* a: Lower bound of the interval for random integers (default is a=1). 
* b: Upper bound of the interval for random integers (default is b=100).

**Output:** These routines all return an n x n square matrix (whether it be a regular square matrix, upper triangular,
lower triangular, or diagonal) where all nonzero entries are in the specified interval [a,b] (default is [1,100]).

**Usage/Example:**

We can implement the following code to generate a 4 x 4 square, upper triangular, lower triangular, and diagonal matrix
respectively with random integers in the interval [-10,10].
```python
import numpy as np


square = np.asarray(square(4, -10, 10), np.float)
upper = np.asarray(upr_trng(4, -10, 10), np.float)
lower = np.asarray(lwr_trng(4, -10, 10), np.float)
diagonal = np.asarray(diag(4, -10, 10), np.float)
print(f'Square:\n{square}\nUpper Triangular:\n{upper}\nLower Triangular:\n{lower}\nDiagonal:\n'
      f'{diagonal}')
```
Output from the lines above:
```python
Square:
[[-8.  7. -5.  0.]
 [ 7.  7.  7.  1.]
 [-8. -8.  8.  0.]
 [-8.  1.  9. -4.]]
Upper Triangular:
[[-3.  8. -4. 10.]
 [ 0.  3.  0.  9.]
 [ 0.  0.  5. -7.]
 [ 0.  0.  0.  1.]]
Lower Triangular:
[[ -7.   0.   0.   0.]
 [ -2.  10.   0.   0.]
 [ -1.   3. -10.   0.]
 [  3.   3.  -4.   7.]]
Diagonal:
[[10.  0.  0.  0.]
 [ 0. 10.  0.  0.]
 [ 0.  0. -4.  0.]
 [ 0.  0.  0. -7.]]
```
As we can see, all matrices above satisfy the conditions for their respective type.

**Implementation/Code:** The following is the code for square(n, a, b), upr_trng(n, a, b), lwr_trng(n, a, b), and
diag(n, a, b) respectively
```python
import random


def square(n, a=1, b=100):
    # initialize array
    A = []
    # Transform A into an n x n matrix of zeroes
    for i in range(n):
        A.append([0 for row in range(n)])
    # Change each value of the matrix to random integer in the interval [a,b]
    for j in range(n):
        for k in range(n):
            A[j][k] = random.randint(a, b)
    # Return the square matrix
    return A


def upr_trng(n, a=1, b=100):
    # Initialize array
    A = []
    # Transform A into an n x n matrix of zeroes
    for i in range(n):
        A.append([0 for row in range(n)])
    # Change each value of the upper triangular portion to a random integer in the interval [a,b]
    for j in range(n):
        for k in range(j, n):
            A[j][k] = random.randint(a, b)
    # Return the upper triangular matrix
    return A


def lwr_trng(n, a=1, b=100):
    # Initialize array
    A = []
    # Transform A into an n x n matrix of zeroes
    for i in range(n):
        A.append([0 for row in range(n)])
    # Change each value of the lower triangular portion to a random integer in the interval [a,b]
    for j in range(n):
        for k in range(j + 1):
            A[j][k] = random.randint(a, b)
    # Return the lower triangular matrix
    return A


def diag(n, a=1, b=100):
    # Initialize array
    A = []
    # Transform A into an n x n matrix of zeroes
    for i in range(n):
        A.append([0 for k in range(n)])
    # Change each diagonal element to a random integer in the interval [a,b]
    for j in range(n):
        A[j][j] = random.randint(a, b)
    # Return the diagonal matrix
    return A
```
**Last Modified:** November/2021

<hr>

[Previous](frwrdsub.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](gauss.md)

<hr>
