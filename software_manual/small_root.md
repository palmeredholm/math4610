# Method to Find Closest Root

**Routine Name:** small_root

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine approximates the root of a function closest to a specified value. This method uses
the hybrid method; therefore, the first derivative of the function will have to be supplied.

**Input:** There are eight input variables in this routine:

* a: Lower bound of the search interval.
* b: Upper bound of the search interval.
* n: Number of subintervals to create when searching for roots.
* x0: Return the root closest to this value.
* f: The objective function. Should be passed in as an anonymous function via the use of a lambda function (e.g., lambda x: x**2).
* df: First derivative of f.
* tol: Desired tolerance in precision of approximation.
* max_iter: Maximum iterations to perform if tolerance is too low to achieve.

**Output:** This routine returns an approximated value of the root closest to x0.

**Usage/Example:**

If we want to find the of the function <img src="https://render.githubusercontent.com/render/math?math=e^{-x^2}\sin(4x^2-1.0)+0.051"> 
closest to 0, for example, we can run the following code with 0.0001 precision, 1,000 subintervals, and an initial interval
of [-5.0,6.0]:

```python
f = lambda x: np.exp(-x**2)*np.sin(4*x**2-1.0)+0.051

df = lambda x: -2*x*np.exp(-x**2)*np.sin(4*x**2-1)+8*x*np.exp(-x**2)*np.cos(4*x**2-1)

print(small_root(-5.0, 6.0, 1000, 0.0, f, df, 0.0001, 100))
```

Output from the code above:

```python
0.4836106985428367
```

**Implementation/Code:** The following is the code for small_root(a, b, n, x0, f, df, tol, max_iter)

```python
import numpy as np
import hybrid


def small_root(a, b, n, x0, f, df, tol, max_iter):
    # Initialize arrays to bracket the interval, store intervals that contain roots, and store roots
    brackets = []
    intervals = []
    roots = []
    # Create partition size for bracketing
    h = (b-a)/n
    # Bracket the interval
    for i in range(n):
        brackets.append([a + i * h, a + (i + 1) * h])
    # Append bracketed interval to interval array if the interval contains a root
    for j in range(len(brackets)):
        if f(brackets[j][0]) * f(brackets[j][1]) < 0:
            intervals.append([brackets[j][0], brackets[j][1]])
    # Append the roots of the intervals to the roots array
    for k in range(len(intervals)):
        roots.append(hybrid.hybrid(intervals[k][0], intervals[k][1], x0, f, df, tol, max_iter))
    # Initialize first element for comparison
    zero = abs(roots[0])
    # Find closest root to the value x0
    for root in range(1, len(roots)):
        if abs(roots[root] - x0) <= zero:
            zero = abs(roots[root])
    # Return closest root to x0
    return zero
```

**Last Modified:** November/2021

<hr>

[Previous](hybrid.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](roots.md)

<hr>
