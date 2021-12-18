# The Inverse Power Method

**Routine Name:** inv_power

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the smallest eigenvalue in magnitude of a matrix down to a specified level
of precision. This routine comes in handy when computing the 2-matrix norm. This is a very robust method as the accumulation
of round-off error helps.

**Input:** This routine has five input variables:

* A: The coefficient matrix.
* x0: A vector conformable with A.
* egval0: An initial guess of the largest eigenvalue in magnitude.
* tol: Specified tolerance level.
* max_iter: Maximum number of iterations to perform.


**Output:** This routine returns an eigenvalue that is the approximated smallest eigenvalue in magnitude using the Rayleigh quotient.

**Usage/Example:**

The following code uses the power method on a random 100 X 100 diagonally dominant matrix.
```python
from more_matgen import diag_dom


A = diag_dom(100)
x0 = [1 for i in range(100)]
print(inv_power(A, x0, 10, 0.000001, 1000))
```
Output from the lines above:
```python
0.0024574463303040925
```
The result above is the smallest eigenvalue in magnitude of the random 100 X 100 diagonally dominant matrix generated.

**Implementation/Code:** The following is the code for inv_power(A, x0, egval0, tol max_iter)
```python
from norms import norm_2
from vectors import vec_scalar, dot_prod
from solve import solve
from more_matgen import diag_dom


def inv_power(A, x0, egval0, tol, max_iter):
    error = 10.0 * tol
    icnt = 0
    while error > tol and icnt < max_iter:
        y = solve(A, x0)
        v = vec_scalar((1 / norm_2(y)), y)
        egval1 = dot_prod(v, solve(A, v))
        error = abs(egval1 - egval0)
        egval0 = egval1
        for i in range(len(v)):
            x0[i] = v[i]
        icnt += 1
    return 1 / egval1
```
**Last Modified:** December/2021

<hr>

[Previous](power.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](mat_norm_l1.md)

<hr>
