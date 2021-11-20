import random


def square(n, a=1, b=100):
    # initialize array
    A = []
    # Transform A into an n x n matrix of zeroes
    for i in range(n):
        A.append([0 for row in range(n)])
    # Change each value of the matrix to random integer in the interval [a,b]
    for j in range(n):
        for k in range(n):
            A[j][k] = random.randint(a, b)
    # Return the square matrix
    return A


def upr_trng(n, a=1, b=100):
    # Initialize array
    A = []
    # Transform A into an n x n matrix of zeroes
    for i in range(n):
        A.append([0 for row in range(n)])
    # Change each value of the upper triangular portion to a random integer in the interval [a,b]
    for j in range(n):
        for k in range(j, n):
            A[j][k] = random.randint(a, b)
    # Return the upper triangular matrix
    return A


def lwr_trng(n, a=1, b=100):
    # Initialize array
    A = []
    # Transform A into an n x n matrix of zeroes
    for i in range(n):
        A.append([0 for row in range(n)])
    # Change each value of the lower triangular portion to a random integer in the interval [a,b]
    for j in range(n):
        for k in range(j + 1):
            A[j][k] = random.randint(a, b)
    # Return the lower triangular matrix
    return A


def diag(n, a=1, b=100):
    # Initialize array
    A = []
    # Transform A into an n x n matrix of zeroes
    for i in range(n):
        A.append([0 for k in range(n)])
    # Change each diagonal element to a random integer in the interval [a,b]
    for j in range(n):
        A[j][j] = random.randint(a, b)
    # Return the diagonal matrix
    return A
