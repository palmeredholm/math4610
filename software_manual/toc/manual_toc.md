## MATH 4610

### Software Manual Table of Contents

<hr>

The following list includes links to extensive documentation for all code written for tasksheets. Click [here](../../README.md) to go back to the home page.

<hr>

* **Entry 1.** [Single Precision Machine Epsilon:](../smaceps.md)
```
This routine will compute the single precision value for the machine epsilon or the number of
digits in the representation of real numbers in single precision. This is a routine for analyzing
the behavior of any computer. This usually will need to be run one time for each computer...
```
* **Entry 2.** [Double Precision Machine Epsilon:](../dmaceps.md)
```
This routine will compute the double precision value for the machine epsilon or the number of
digits in the representation of real numbers in single precision. This is a routine for analyzing
the behavior of any computer. This usually will need to be run one time for each computer...
```
* **Entry 3.** [Absolute Error:](../abserror.md)
```
This routine will compute the absolute error in approximating a number, x, with another number,
y. This is a routine for computing the accuracy of an estimate...
```
* **Entry 4.** [Relative Error:](../relerror.md)
```
This routine will compute the relative error in approximating a number, x, with another number,
y. This is a routine for computing the accuracy of an estimate...
```
* **Entry 5.** [Python Graphics in Matplotlib:](../graphics.md)
```
This routine will graph functions using Matplotlib. This routine can be used to compare the
graphs of different functions to analyze their properties...
```
* **Entry 6.** [Fixed Point Iteration:](../fxd_pt_iter.md)
```
This routine will compute the root of a function using fixed point iteration. With a good guess
(i.e., a point close to a root of the function), the routine will return an approximation of the
closest root to the guess...
```
* **Entry 7.** [Bisection:](../bisection.md)
```
This routine will compute the root of a function using the bisection method. As long as we know
that there exists one root in some interval, via the intermediate value theorem, we can
approximate the value of that root down to a specified precision level...
```
* **Entry 8.** [Newton's Method:](../newton.md)
```
This routine will compute the root of a function using Newton's method. As long as we know a
point in the function that is close enough to a root and the first derivative of the function,
we can approximate the root down to a specified precision level...
```
* **Entry 9.** [Secant Method](../secant.md)
```
This routine will compute the root of a function using the Secant method. As long as we know two
points in the function that are close enough to a root, we can approximate the root down to a
specified precision level...
```
* **Entry 10.** [Hybrid Newton-Bisection Method](../hybrid.md)
```
This routine is a more robust root finding method that combines a bisection step to Newton's
method to approximate roots. As long as we know an interval that contains at most one root, and
an initial guess that is close enough to a root (provided we can calculate the first derivative),
a root can be approximated...
```
* **Entry 11.** [Hybrid Newton-Secant Method](../hybrid_secant.md)
```
This routine is a more robust root finding method that combines a bisection step to the secant
method to approximate roots. If after one iteration of Newton's method, the error increases,
the routine performs four iterations of bisection to reduce the error. As long as we know an
interval that contains at most one root, and two initial guesses that are close enough to a
root, a root can be approximated...
```
* **Entry 12.** [Method to Find Closest Root](../small_root.md)
```
This routine approximates the root of a function closest to a specified value. Approaches using
both hybrid methods are shown. In the case of the newton-bisection hybrid method, the first
derivative will need to be supplied...
```
* **Entry 13.** [Method to Find All Roots of a Function](../roots.md)
```
This routine approximates all the routes contained in a specified interval of a given function. 
This method uses the hybrid method; therefore, therefore the first derivative of the function
will have to be supplied...
```

<hr>
