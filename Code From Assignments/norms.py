def norm_1(x):
    # Initialize sum variable
    norm = 0
    # Traverse the vector and sum the absolute values
    for i in range(len(x)):
        norm += abs(x[i])
    # Return l1 norm
    return norm


def norm_2(x):
    # Initialize sum variable
    norm = 0
    # Traverse the vector and sum the squares
    for i in range(len(x)):
        norm += float(x[i]) * float(x[i])
    # Return the square of the sum of the squares (i.e., the l2 norm)
    return norm ** 0.5


def norm_inf(x):
    # Return the largest absolute value element (i.e., the l infinity norm)
    return max(x, key=abs)
