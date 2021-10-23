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

print(newton(1.0, lambda x: x*np.e**(3*x**2)-7*x, lambda x: np.e**(3*x**2)+6*(x**2)*np.e**(3*x**2)-7, 0.0001, 10))
