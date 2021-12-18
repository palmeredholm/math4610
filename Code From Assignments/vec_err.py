from vectors import vec_subtract
from norms import norm_1, norm_2, norm_inf


def err_1(x, y):
    # Check to see if vectors are conformable
    if len(x) != len(y):
        raise Exception('Non-conformable arrays')
    # Return the l1 error between x and y
    return norm_1(vec_subtract(x, y))


def err_2(x, y):
    # Check to see if vectors are conformable
    if len(x) != len(y):
        raise Exception('Non-conformable arrays')
    # Return the l2 error between x and y
    return norm_2(vec_subtract(x, y))


def err_inf(x, y):
    # Check to see if vectors are conformable
    if len(x) != len(y):
        raise Exception('Non-conformable arrays')
    # Return the l infinity error between x and y
    return norm_inf(vec_subtract(x, y))
