import numpy as np

def hybrid_secant(a, b, x0, x1, f, tol, max_iter):
    # Initialize needed variables
    fa = f(a)
    fb = f(b)
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        raise Exception('Zero not contained in the interval')
    if x0 < a or x0 > b:
        x0 = 0.5*(a+b)
    f0 = f(x0)
    f1 = f(x1)
    error = 10.0*tol
    errsec = 10.0*tol
    icnt = 0
    # Start secant method
    while errsec > tol and icnt < max_iter:
        x2 = x1 - f1*(x1 - x0)/(f1 - f0)
        errsec = abs(x2-x1)
        # Perform 4 iterations of secant method if needed
        if errsec > error:
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
            x1 = x2
            f0 = f(c)
            f1 = f(x1)
        else:
            x0 = x1
            x1 = x2
            f0 = f(x0)
            f1 = f(x1)
        icnt += 1
    return x2

f = lambda x: np.exp(-x**2)*np.sin(4*x**2-1.0)+0.051

print(hybrid_secant(0.0, 0.9, 0.3, 0.7, f, 0.0001, 100))