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
