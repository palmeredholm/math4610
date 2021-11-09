# Method to Find All Roots of a Function

**Routine Name:** roots

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine approximates all the routes contained in a specified interval of a given function. 
This method uses the hybrid method; therefore, therefore the first derivative of the function will have to be supplied.

**Input:** There are eight input variables in this routine:

* a: Lower bound of the search interval.
* b: Upper bound of the search interval.
* n: Number of subintervals to create when searching for roots.
* x0: Initial guess at a root contained in the function.
* f: The objective function. Should be passed in as an anonymous function via the use of a lambda function (e.g., lambda x: x**2).
* df: First derivative of f.
* tol: Desired tolerance in precision of approximation.
* max_iter: Maximum iterations to perform if tolerance is too low to achieve.

**Output:** This routine returns an array of approximations of all roots found within the specified interval of f.

**Usage/Example:**

If we want to find the roots of the function <img src="https://render.githubusercontent.com/render/math?math=e^{-x^2}\sin(4x^2-1.0)+0.051">, 
for example, we can first graph it to see where the roots lie.

![alt text](sheet6.png)

As we can see, all the roots lie in the interval [-2.0,2.0]. Just to be safe, we'll consider the interval [-5.0,6.0].
The following code will print out approximations of all the roots contained in that interval with precision 0.0001 and 1,000
subintervals:

```python
f = lambda x: np.exp(-x**2)*np.sin(4*x**2-1.0)+0.051

df = lambda x: -2*x*np.exp(-x**2)*np.sin(4*x**2-1)+8*x*np.exp(-x**2)*np.cos(4*x**2-1)

print(num_roots(-5.0, 6.0, 1000, 0.0, f, df, 0.0001, 100))
```

Output from the code above:

```python
[-1.7229455793710828, -1.7051042074233391, -1.3215861833430567, -1.0357671062554235, -0.48361069854284117, 0.4836106985428367, 1.0357671062567162, 1.321586182968371, 1.7051041903953095, 1.7229455786568437]
```

**Implementation/Code:** The following is the code for roots(a, b, n, x0, f, df, tol, max_iter)

```python
import hybrid
import numpy as np


def num_roots(a, b, n, x0, f, df, tol, max_iter):
    # Initialize arrays to bracket the interval, store intervals that contain roots, and store roots
    brackets = []
    intervals = []
    roots = []
    # Create a partition size for bracketing
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
    # Return array of all roots in [a,b]
    return roots
```

**Last Modified:** November/2021

<hr>

[Previous](small_root.md)
| [Table of Contents](toc/manual_toc.md)
| [Next]()

<hr>
