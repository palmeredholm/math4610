import numpy as np

def smaceps():
    # Initialize variables to compute the machine value
    # near 1
    one = np.single(1)
    seps = np.single(1)
    appone = np.single(one + seps)
    # Loop, dividing by 2 each time to determine when the
    # difference between one and the approximation is zero
    # in single precision
    ipow = 0
    # Break out of the loop if the comparison is small
    # enough
    while abs(appone - one) != np.single(0):
        ipow += 1
        # Update the perturbation and compute the
        # approximation to one
        seps = np.single(seps / 2)
        appone = one + seps
    return f'Bits: {ipow}, Value: {seps}'

print(smaceps())