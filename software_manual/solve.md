# Solving Square Linear Systems of Equations

**Routine Name:** solve

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine implements the Gaussian elimination and back substitution methods to solve square
linear systems of equations. This method assumes that the system has a unique solution.

**Input:** This routine has two input variables:

* A: Nonsingular coefficient matrix to a system of equations.
* b: b vector in the system of equations.

**Output:** This routine returns the vector x which is the solution to the system of equations.

**Usage/Example:**

We can implement the following code to solve a 5 x 5 system of equations with a diagonally dominant coefficient matrix
with entries in the interval [-20,20]. For simplicity, our b vector will be a vector of ones.
```python
from backsub import backsub
from gauss import gauss
import random
from more_matgen import diag_dom


A = diag_dom(5, -20, 20)
b = [1 for el in range(5)]
x = solve(A, b)
print('A:')
for row in A:
    print(row)
print(f'b:\n{b}\nx:\n{x}')
```
Output from the lines above:
```python
A:
[12, -8, -1, 3, 0]
[-10, 12, 1, 0, 0]
[1, -3, -17, -8, 0]
[-4, 6, 1, -13, 1]
[8, 0, 0, -1, -9]
b:
[1, 1, 1, 1, 1]
x:
[ 0.30954591  0.34958589 -0.09957161 -0.00581179  0.16468656]
```
Above, we can see what the diagonally dominant coefficient matrix looks like, the b vector, and the solution to the system
of equations x.

**Implementation/Code:** The following is the code for solve(A, b)
```python
from backsub import backsub
from gauss import gauss
from more_matgen import diag_dom


def solve(A, b):
    row_ech = gauss(A, b)
    A, b = row_ech[0], row_ech[1]
    return backsub(A, b)
```
**Last Modified:** November/2021

<hr>

[Previous](more_matgen.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](lu.md)

<hr>
