import random


def diag_dom(n, a=-10, b=10):
    A = []
    for i in range(n):
        A.append([0 for row in range(n)])
    for j in range(n):
        A[j][j] = random.randint(a, b)
    for k in range(n):
        for l in range(n):
            if k == l:
                continue
            else:
                comp = abs(A[k][k]) - abs(abs(A[k][k]) - sum(abs(el) for el in A[k]))
                A[k][l] = random.randint(-comp, comp)
    return A


def hilbert(n):
    H = []
    for i in range(n):
        H.append([(1/(i + j + 1)) for j in range(n)])
    return H