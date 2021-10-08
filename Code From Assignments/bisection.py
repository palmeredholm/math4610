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
