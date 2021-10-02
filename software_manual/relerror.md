# Relative Error

**Routine Name:**           rel_error

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This routine will compute the relative error in approximating a number, x, with another number, y. This is a routine for computing the accuracy of an estimate.

**Input:** There are two input variables needed for this routine. The first variable, x, is the number to be approximated. The second variable, y, is the number used to approximate x.

**Output:** This routine returns a double precision value for the relative error y when approximating x.

**Usage/Example:**

The routine has two arguments needed to return the relative error when approximating a value. Due to the dynamic nature of Python, if one of the inputs has a decimal place, the result returned will be of double precision. By printing a call to rel_error, we can see what the relative error is when approximating 1.0 with 0.9.
```
print(rel_error(1.0, 0.9))
```
Output from the line above:
```
0.09999999999999998
```
The relative error when approximating 1.0 with 0.9 is the double precision value given above.

**Implementation/Code:** The following is the code for rel_error(x, y)
```
def rel_error(x, y):
    # Find relative error in approximating x with y
    output = (abs(y - x) / abs(x))
    return output
```
**Last Modified:** October/2021

<hr>

[Previous](abserror.md)
| [Table of Contents](toc/manual_toc.md)
| [Next](graphics.md)

<hr>
