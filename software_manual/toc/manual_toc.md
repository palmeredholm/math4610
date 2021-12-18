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
* **Entry 9.** [Secant Method:](../secant.md)
```
This routine will compute the root of a function using the Secant method. As long as we know two
points in the function that are close enough to a root, we can approximate the root down to a
specified precision level...
```
* **Entry 10.** [Hybrid Newton-Bisection Method:](../hybrid.md)
```
This routine is a more robust root finding method that combines a bisection step to Newton's
method to approximate roots. As long as we know an interval that contains at most one root, and
an initial guess that is close enough to a root (provided we can calculate the first derivative),
a root can be approximated...
```
* **Entry 11.** [Hybrid Secant-Bisection Method:](../hybrid_secant.md)
```
This routine is a more robust root finding method that combines a bisection step to the secant
method to approximate roots. If after one iteration of Newton's method, the error increases,
the routine performs four iterations of bisection to reduce the error. As long as we know an
interval that contains at most one root, and two initial guesses that are close enough to a
root, a root can be approximated...
```
* **Entry 12.** [Method to Find Closest Root:](../small_root.md)
```
This routine approximates the root of a function closest to a specified value. Approaches using
both hybrid methods are shown. In the case of the newton-bisection hybrid method, the first
derivative will need to be supplied...
```
* **Entry 13.** [Method to Find All Roots of a Function:](../roots.md)
```
This routine approximates all the routes contained in a specified interval of a given function. 
This method uses the hybrid method; therefore, therefore the first derivative of the function
will have to be supplied...
```
* **Entry 14.** [Back Substitution:](../backsub.md)
```
This routine will compute the solution to a system of equations once that system has already
been reduced to upper triangular. This routine uses back substitution to solve for the unkowns
of the system. This routine assumes that the matrix passed in is already in upper triangular...
```
* **Entry 15.** [Forward Substitution:](../frwrdsub.md)
```
This routine will compute the solution to a system of equations once that system has already
been reduced to lower triangular. This routine uses forward substitution to solve for the
unkowns of the system. This routine assumes that the matrix passed in is already in lower
triangular...
```
* **Entry 16.** [Random Matrix Generation:](../matgen.md)
```
These four routines are all very similar to each other. Each one creates a square matrix with
specified random integers for each element, the upper triangular portion, the lower triangular
portion, or the diagonal elements...
```
* **Entry 17.** [Gaussian Elimination:](../gauss.md)
```
This routine performs Guassian elimination on an augmented matrix to reduce it to row echelon
form. This routine assumes that the matrix is nonsingular...
```
* **Entry 18.** [More Matrix Generation:](../more_matgen.md)
```
These two routines create a random diagonally dominant matrix and a Hilbert matrix respectively.
The size of both is determined by the value passed in. The nonzero elements of the diagonally
dominant matrix are according to the interval that is passed in...
```
* **Entry 19.** [Solving Square Linear Systems of Equations:](../solve.md)
```
This routine implements the Gaussian elimination and back substitution methods to solve square
linear systems of equations. This method assumes that the system has a unique solution...
```
* **Entry 20.** [LU Factorization:](../lu.md)
```
This routine computes the LU factorization of a given matrix. LU factorization is extremely
helpful for many computational problems that often arise...
```
* **Entry 21.** [Scaled Partial Pivoting:](../sc_part_pivot.md)
```
This routine also computes the LU factorization of a given matrix. However, this routine
utilizes scaled partial pivoting to deal with problems that are not very well-conditioned...
```
* **Entry 22.** [Vector Addition:](../vec_add.md)
```
This routine will computes the vector addition of two conformable vectors...
```
* **Entry 23.** [Vector Subtraction:](../vec_subtract.md)
```
This routine will computes the vector subtraction of two conformable vectors...
```
* **Entry 24.** [Scalar Multiplication for Vectors:](../vec_scalar.md)
```
This routine will compute the scalar multiplication for a scalar and a vector...
```
* **Entry 25.** [Vector Dot Product:](../vec_dot_prod.md)
```
his routine will compute the dot product of two conformable vectors...
```
* **Entry 26.** [Outer Product:](../outer_product.md)
```
This routine will compute the outer product of two conformable vectors...
```
* **Entry 27.** [Vector 1-Norm:](../vec_mag_l1.md)
```
This routine will compute the 1-norm of a vector. The 1-norm is an alternative way of
measuring the magnitude of a vector...
```
* **Entry 28.** [Vector 2-Norm:](../vec_mag_l2.md)
```
This routine will compute the 2-norm of a vector. The 1-norm is an alternative way of
measuring the magnitude of a vector...
```
* **Entry 29.** [Vector Infinity-Norm:](../vec_mag_linf.md)
```
This routine will compute the infinity-norm of a vector. The infinity-norm is an
alternative way of measuring the magnitude of a vector...
```
* **Entry 30.** [Vector Difference 1-Norm:](../vec_err_l1.md)
```
This routine will compute the error between two vectors using the 1-norm...
```
* **Entry 31.** [Vector Difference 2-Norm:](../vec_err_l2.md)
```
This routine will compute the error between two vectors using the 2-norm...
```
* **Entry 32.** [Vector Difference Infinity-Norm:](../vec_err_linf.md)
```
This routine will compute the error between two vectors using the infinity-norm...
```
* **Entry 33.** [Matrix Addition:](../mat_add.md)
```
This routine will compute the matrix addition of two conformable matrices...
```
* **Entry 34.** [Matrix Subtraction:](../mat_subtract.md)
```
This routine will compute the matrix subtraction of two conformable matrices...
```
* **Entry 35.** [Scalar Multiplication for Matrices:](../mat_scalar.md)
```
This routine will compute the scalar multiplication for a scalar and a matrix...
```
* **Entry 36.** [Matrix Transpose:](../mat_transpose.md)
```
This routine will compute the transpose of a given matrix...
```
* **Entry 37.** [Dot Product of a Matrix and a Vector:](../mat_vec_prod.md)
```
This routine will compute the dot product of a conformable matrix and vector...
```
* **Entry 38.** [Matrix Dot Product:](../mat_prod.md)
```
This routine will compute the dot product of two conformable, rectangular matrices...
```
* **Entry 39.** [Jacobi Iteration:](../jacobi.md)
```
This is a routine that solves a linear system of equation through Jacobi iteration. Jacobi
iteration is less accurate than the other methods listed because it is only an approximation;
however, it is a much faster and more robust method for solving linear systems...
```
* **Entry 40.** [The Power Method:](../power.md)
```
This routine will compute the largest eigenvalue in magnitude of a matrix down to a specified
level of precision. This routine comes in handy when computing the 2-matrix norm. This is a very
robust method as the accumulation of round-off error helps...
```
* **Entry 41.** [The Inverse Power Method:](../inv_power.md)
```
This routine will compute the smallest eigenvalue in magnitude of a matrix down to a specified
level of precision. This routine comes in handy when computing the 2-matrix norm. This is a very
robust method as the accumulation ..of round-off error helps.
```
* **Entry 42.** [1-Matrix Norm:](../mat_norm_l1.md)
```
This routine computes the 1-norm of a matrix which is simply the largest absolute value column
sum of a matrix...
```
* **Entry 43.** [Infinity-Matrix Norm:](../mat_norm_linf.md)
```
This routine computes the infinity-norm of a matrix which is simply the largest absolute value
row sum of a matrix...
```
* **Entry 44.** [2-Matrix Norm:](../mat_norm_l2.md)
```
This routine computes the 2-norm of a matrix which is also known as the spectral norm. This
routine simply computes the largest singular value of a matrix...
```
* **Entry 45.** [Parallelism](../parallel.md)
```

```

<hr>
