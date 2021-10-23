import numpy as np

def secant(x0, x1, f, tol, max_iter):
    # Initialize needed variables
    f0 = f(x0)
    f1 = f(x1)
    error = 10*tol
    icnt = 0
    # Create loop to perform secant method
    while error > tol and icnt < max_iter:
        x2 = x1 - f1*(x1 - x0)/(f1 - f0)
        error = abs(x2-x1)
        icnt += 1
        x0 = x1
        x1 = x2
        f0 = f(x0)
        f1 = f(x1)
    return x2

print(secant(0.5, 1, lambda x: x*np.e**(3*x**2)-7*x, 0.0001, 100))
