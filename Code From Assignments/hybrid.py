import numpy as np

def hybrid(a, b, x0, f, df, tol, max_iter):
    # Initialize needed variables
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise Exception('Root not in interval')
    if x0 < a or x0 > b:
        raise Exception('Invalid initial guess')
    f0 = f(x0)
    df0 = df(x0)
    error = 10.0*tol
    errnewt = 10.0*tol
    icnt = 0
    # Start Newton's method
    while errnewt > tol and icnt < max_iter:
        x1 = x0-f0/df0
        errnewt = abs(x1-x0)
        # Perform 4 iterations of bisection if needed
        if errnewt > error:
            for i in range(4):
                c = 0.5*(a+b)
                fc = f(c)
                if fa*fc < 0:
                    b = c
                    fb = fc
                else:
                    a = c
                    fa = fc
            error = abs(b-a)
            x0 = c
            f0 = f(c)
            df0 = df(c)
        else:
            x0 = x1
            f0 = f(x0)
            df0 = df(x0)
        icnt += 1
    return x1
