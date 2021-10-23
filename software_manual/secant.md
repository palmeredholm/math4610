# Secant Method

**Routine Name:** secant

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the root of a function using the Secant method. As long as we know two points in the function that are close enough to a root, we can approximate the root down to a specified precision level.

**Input:** There are five input variables in this routine:

* x0: An initial guess that is close enough to the root.
* x1: Another initial guess that is close enough to the root.
* f: The objective function. Should be passed in as an anonymous function via the use of a lambda function (e.g., lambda x: x**2).
* tol: Desired tolerance in precision of approximation.
* max_iter: Maximum number of iterations to perform if tolerance level is too small.

**Output:** This routine returns a double precision estimate of the root closest to x0 and x1.

**Usage/Example:**

If we want to find a root of the function <img src="https://render.githubusercontent.com/render/math?math=xe^{3x^2}-7x">, we can first graph it to see where the roots lie.

![alt text](sheet4_3.png)

As we can see, there is a root somewhere in the interval [0.5,1]. We can run the following code to estimate that root.

```python
print(secant(0.5, 1, lambda x: x*np.e**(3*x**2)-7*x, 0.0001, 100))
```

Output from the lines above:

```python
0.8053798245521222
```

The above value is the approximate root of the function in the interval [0.5,1].

**Implementation/Code:** The following is the code for secant(x0, x1, f, tol, max_iter)

```python
import numpy as np

def secant(x0, x1, f, tol, max_iter):
    # Initialize needed variables
    f0 = f(x0)
    f1 = f(x1)
    error = 10*tol
    icnt = 0
    # Create loop to perform secant method
    while error > tol and icnt < max_iter:
        x2 = x1 - f1*(x1 - x0)/(f1 - f0)
        error = abs(x2-x1)
        icnt += 1
        x0 = x1
        x1 = x2
        f0 = f(x0)
        f1 = f(x1)
    return x2
```

**Last Modified:** October/2021

<hr>

[Previous](newton.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](hybrid.md)

<hr>
