# The Power Method

**Routine Name:** power

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the largest eigenvalue in magnitude of a matrix down to a specified level
of precision. This routine comes in handy when computing the 2-matrix norm. This is a very robust method as the accumulation
of round-off error helps.

**Input:** This routine has five input variables:

* A: The coefficient matrix.
* x0: A vector conformable with A.
* egval0: An initial guess of the largest eigenvalue in magnitude.
* tol: Specified tolerance level.
* max_iter: Maximum number of iterations to perform.


**Output:** This routine returns an eigenvalue that is the approximated largest eigenvalue in magnitude using the Rayleigh quotient.

**Usage/Example:**

The following code uses the power method on a random 100 X 100 diagonally dominant matrix.
```python
from more_matgen import diag_dom


A = diag_dom(100, -100, 100)
x0 = [50 for i in range(100)]
print(power(A, x0, 100, 0.0001, 10000))
```
Output from the lines above:
```python
128.39811766013023
```
The result above is the largest eigenvalue in magnitude of the random 100 X 100 diagonally dominant matrix generated.

**Implementation/Code:** The following is the code for power(A, x0, egval0, tol, max_iter)
```python
from matrix_ops import mat_vec_prod
from vectors import vec_scalar, dot_prod
from norms import norm_2


def power(A, x0, egval0, tol, max_iter):
    error = 10.0 * tol
    icnt = 0
    y = mat_vec_prod(A, x0)
    w = vec_scalar((1 / norm_2(y)), y)
    while error > tol and icnt < max_iter:
        q = mat_vec_prod(A, w)
        egval1 = dot_prod(w, q)
        error = abs(egval1 - egval0)
        for i in range(len(w)):
            x0[i] = w[i]
        egval0 = egval1
        w = vec_scalar((1 / norm_2(q)), q)
        icnt += 1
    return egval1
```
**Last Modified:** December/2021

<hr>

[Previous](jacobi.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](inv_power.md)

<hr>
