def abs_error(x, y):
    # Find absolute error in approximating x with y
    output = abs(x - y)
    return output


def rel_error(x, y):
    # Find relative error in approximating x with y
    output = (abs(y - x) / abs(x))
    return output

