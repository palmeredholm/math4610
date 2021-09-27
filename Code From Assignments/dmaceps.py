def dmaceps():
    # Initialize variables to compute the machine value
    # near 1.0
    one = 1.0
    seps = 1.0
    appone = one + seps
    # Loop, dividing by 2 each time to determine when the
    # difference between one and the approximation is zero
    # in double precision
    ipow = 0
    # Break out of the loop if the comparison is small
    # enough
    while abs(appone - one) != 0.0:
        ipow += 1
        # Update the perturbation and compute the
        # approximation to one
        seps = seps / 2
        appone = one + seps
    return f'Bits: {ipow}, Value: {seps}'

print(dmaceps())