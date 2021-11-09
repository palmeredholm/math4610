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
