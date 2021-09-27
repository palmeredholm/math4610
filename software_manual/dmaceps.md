# Double Precision Machine Epsilon

**Routine Name:**           dmaceps

**Author:** Palmer Edholm

**Language:** Python

**Description/Purpose:** This routine will compute the double precision value for the machine epsilon or the number of digits
in the representation of real numbers in single precision. This is a routine for analyzing the behavior of any computer. This
usually will need to be run one time for each computer.

**Input:** There are no inputs needed in this case.

**Output:** This routine returns a single precision value for the number of decimal digits that can be represented on the
computer being queried.

**Usage/Example:**

We can print the call to the function dmaceps

      print(dmaceps())

Output from the lines above:

      Bits: 53, Value: 1.1102230246251565e-16

The first value (53) is the number of binary digits that define the machine epsilon and the second is related to the
decimal version of the same value. The number of decimal digits that can be represented is roughly sixteen (E-16 on the
end of the second value).

**Implementation/Code:** The following is the code for smaceps()

 ```
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
 ```

**Last Modified:** September/2021

<hr>

[Previous](smaceps.md)
| [Table of Contents](toc/manual_toc.md)

<hr>
