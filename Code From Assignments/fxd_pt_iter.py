import numpy as np


def fxd_pt_iter(x0, f, tol, max_iter):
    def g(x):
        return x-(10**(-2))*f(x)
    iters = 0
    error = 10 * max_iter
    while error > tol and iters < max_iter:
        x1 = g(x0)
        error = abs(x1-x0)
        x0 = x1
        iters += 1
    return x1, iters
