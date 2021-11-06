# Single Precision Machine Epsilon

**Routine Name:**           smaceps

**Author:** Palmer Edholm

**Language:** Python

**Description/Purpose:** This routine will compute the single precision value for the machine epsilon or the number of digits
in the representation of real numbers in single precision. This is a routine for analyzing the behavior of any computer. This
usually will need to be run one time for each computer.

**Input:** There are no inputs needed in this case.

**Output:** This routine returns a single precision value for the number of decimal digits that can be represented on the
computer being queried.

**Usage/Example:**

We can print the call to the function smaceps:
```python
print(smaceps())
```
Output from the line above:

      Bits: 24, Value: 5.960464477539063e-08

The first value (24) is the number of binary digits that define the machine epsilon and the second is related to the
decimal version of the same value. The number of decimal digits that can be represented is roughly eight (E-08 on the
end of the second value).

**Implementation/Code:** The following is the code for smaceps()
```python
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
```
**Last Modified:** September/2021
<hr>

[Table of Contents](toc/manual_toc.md)
| [Next](dmaceps.md)

<hr>
