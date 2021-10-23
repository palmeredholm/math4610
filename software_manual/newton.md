# Newton's Method

**Routine Name:** newton

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the root of a function using Newton's method. As long as we know a point in the function that is close enough to a root and the first derivative of the function, we can approximate the root down to a specified precision level.

**Input:** There are five input variables in this routine:

* x0: An initial guess that is close enough to the root.
* f: The objective function. Should be passed in as an anonymous function via the use of a lambda function (e.g., lambda x: x**2).
* df: The first derivative of the objective function. Should also be passed in as an anonymous function.
* tol: Desired tolerance in precision of approximation.
* max_iter: Maximum number of iterations to perform if tolerance level is too small.

**Output:** This routine returns a double precision estimate of the root closest to x0.

**Usage/Example:**

If we want to find a root of the function <img src="https://render.githubusercontent.com/render/math?math=xe^{3x^2}-7x">, we can first graph it to see where the roots lie.

![alt text](sheet4_3.png)

As we can see, there is a root close to <img src="https://render.githubusercontent.com/render/math?math=x=1">. We can run the following code to estimate that root.

```python
print(newton(1.0, lambda x: x*np.e**(3*x**2)-7*x, lambda x: np.e**(3*x**2)+6*(x**2)*np.e**(3*x**2)-7,
    0.0001, 10))
```

Output from the lines above:

```python
0.8053798692388104
```

The above value is the approximate root of the function near <img src="https://render.githubusercontent.com/render/math?math=x=1">.

**Implementation/Code:** The following is the code for newton(x0, f, df, tol, max_iter)

```python
import numpy as np

def newton(x0, f, df, tol, max_iter):
    # Initialize needed variables
    f0 = f(x0)
    df0 = df(x0)
    error = 10*tol
    icnt = 0
    # Create loop to perform newton's method
    while error > tol and icnt < max_iter:
        x1 = x0 - f0/df0
        error = abs(x1-x0)
        icnt += 1
        x0 = x1
        f0 = f(x0)
        df0 = df(x0)
    return x1
```

**Last Modified:** October/2021

<hr>

[Previous](bisection.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](secant.md)

<hr>
