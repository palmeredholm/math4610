import numpy as np

def hybrid(a, b, x0, f, df, tol, max_iter):
    # Initialize needed variables
    fa = f(a)
    fb = f(b)
    if fa * fb >0:
        raise Exception('Root not in interval')
    if x0 < a or x0 > b:
        raise Exception('Invalid initial guess')
    f0 = f(x0)
    df0 = df(x0)
    error = 10*tol
    icnt=0
    # Start Newton's method
    while error > tol and icnt < max_iter:
        x1 = x0-f0/df0
        errnewt = abs(x1-x0)
        # Perform 4 iterations of bisection if needed
        if errnewt > error:
            for i in range(4):
                c = 0.5*(a+b)
                fc = f(c)
                if fa*fc<0:
                    b=c
                else:
                    a=c
        error = abs(x1-x0)
        x0 = x1
        f0 = f(x0)
        df0 = df(x0)
        icnt += 1
    return x1

print(hybrid(0.5, 1.0, 0.9, lambda x: x*np.e**(3*x**2)-7*x, lambda x: np.e**(3*x**2)+6*(x**2)*np.e**(3*x**2)-7,
             0.0001, 100))
