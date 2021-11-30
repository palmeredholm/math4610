from backsub import backsub
from gauss import gauss


def solve(A, b):
    row_ech = gauss(A, b)
    A, b = row_ech[0], row_ech[1]
    return backsub(A, b)
