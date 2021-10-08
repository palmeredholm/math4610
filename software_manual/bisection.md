# Bisection

**Routine Name:** bisection

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the root of a function using the bisection method. As long as we know that there exists one root in some interval, via the intermediate value theorem, we can approximate the value of that root down to a specified precision level.

**Input:** There are four input variables in this routine:

* a: Lower bound of the closed interval that contains the root.
* b: Upper bound of the closed interval that contains the root.
* f: The objective function. Should be passed in as an anonymous function via the use of a lambda function (e.g., lambda x: x**2).
* tol: Desired tolerance in precision of approximation.

**Output:** This routine returns a double precision estimate of the root contained in the specified interval. The routine calculates how many iterations to perform to achieve the desired level of precision.

**Usage/Example:**

If we want to find a root of the function <img src="https://render.githubusercontent.com/render/math?math=xe^{3x^2}-7x">, we can first graph it to see where the roots lie.

![alt text](sheet4_3.png)

As we can see, there is one root in the closed and bounded interval [0.5, 1.5]. We can run the following code with precision level 0.0001.

      print(bisection(0.5, 1.5, lambda x: x*np.e**(3*x**2)-7*x, 0.0001))

Output from the lines above:

      0.80535888671875

The number above is the approximate root that lies in the interval [0.5, 1.5] with precision of 0.0001.

**Implementation/Code:** The following is the code for bisection(a,b,f,tol)
```
import numpy as np


def bisection(a, b, f, tol):
    fa = f(a)
    fb = f(b)
    if fa*fb > 0:
        raise Exception('Root not in specified interval')
    error = abs(b-a)
    k = int((np.log(error / tol) / np.log(2))+1)
    for i in range(k):
        c = 0.5 * (a+b)
        fc = f(c)
        if fa * fc < 0:
            b = c
        else:
            a = c
    return c
```
**Last Modified:** October/2021

<hr>

[Previous](fxd_pt_iter.md)
| [Table of Contents](toc/manual_toc.md)
| [Next]()

<hr>
