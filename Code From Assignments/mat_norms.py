import numpy as np
from more_matgen import diag_dom
from power import power
from matrix_ops import transpose, mat_prod


def norm_1(A):
    col_sum = sum(abs(el) for el in [col[0] for col in A])
    for i in range(1, len(A)):
        temp_sum = sum(abs(el) for el in [col[i] for col in A])
        if temp_sum > col_sum:
            col_sum = temp_sum
    return col_sum


def norm_inf(A):
    row_sum = sum(abs(el) for el in A[0])
    for i in range(1, len(A)):
        temp_sum = sum(abs(el) for el in A[i])
        if temp_sum > row_sum:
            row_sum = temp_sum
    return row_sum


def norm_2(A):
    A = mat_prod(transpose(A), A)
    return (power(A, [50 for i in range(len(A))], 50, 0.0001, 1000))**0.5


# A = diag_dom(100, -100, 100)
# me = norm_2(A)

A = [[1, -2],
     [3, -4]]
print(norm_2(A))