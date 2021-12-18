from norms import norm_2
from vectors import vec_scalar, dot_prod
from solve import solve
from more_matgen import diag_dom


def inv_power(A, x0, egval0, tol, max_iter):
    error = 10.0 * tol
    icnt = 0
    while error > tol and icnt < max_iter:
        y = solve(A, x0)
        v = vec_scalar((1 / norm_2(y)), y)
        egval1 = dot_prod(v, solve(A, v))
        error = abs(egval1 - egval0)
        egval0 = egval1
        for i in range(len(v)):
            x0[i] = v[i]
        icnt += 1
    return 1 / egval1


A = diag_dom(100)
x0 = [1 for i in range(100)]
print(inv_power(A, x0, 10, 0.000001, 1000))
