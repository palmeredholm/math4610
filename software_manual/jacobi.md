# Jacobi Iteration

**Routine Name:** jacobi

**Author:** Palmer Edholm

**Language:** Python.

**Description/Purpose:** This is a routine that solves a linear system of equation through Jacobi iteration. Jacobi iteration
is less accurate than the other methods listed because it is only an approximation; however, it is a much faster and more
robust method for solving linear systems.

**Input:** This routine has five input variables.

* A: The coefficient matrix of the linear system.
* b: The b vector of the linear system.
* x0: An approximation to the solution vector.
* tol: The tolerance level that must be achieved.
* max_iter: Maximum number of iterations to perform.

**Output:** This routine returns a solution vector to the linear system that is accurate down to a specified tolerance level.

**Usage/Example:**

The following code implements Jacobi iteration on a 100 X 100 diagonally dominant matrix.
```python
from more_matgen import diag_dom
from matrix_ops import mat_vec_prod
import pprint


A = diag_dom(100)
x = [1 for i in range(100)]
b = mat_vec_prod(A, x)
sol_1 = jacobi(A, b, [25 for i in range(100)], 0.00001, 10000)
pprint.pprint(sol_1)
```
Output from the lines above:
```python
[0.9999997578835449,
 0.9999997619406752,
 0.9999997495219957,
 0.9999997275986168,
 0.9999997560380052,
 0.9999997166762558,
 0.9999997589496104,
 0.9999997549798815,
 0.9999997408152593,
 0.9999997478897648,
 0.999999763386844,
 0.9999997576998094,
 0.9999997532720644,
 0.9999997430808334,
 0.9999997349950319,
 0.9999997135972921,
 0.9999997434458728,
 0.9999997362361341,
 0.9999997534624435,
 0.9999997419844365,
 0.9999997471263468,
 0.9999997579814742,
 0.9999997636161928,
 0.9999997260759895,
 0.9999997541217207,
 0.9999997487536716,
 0.9999997587950072,
 0.9999997446162061,
 0.9999997419098546,
 0.9999997421454574,
 0.9999997646719249,
 0.9999997458341614,
 0.9999997747622295,
 0.9999997425185814,
 0.9999997411674079,
 0.9999997514153836,
 0.9999997468279288,
 0.9999997742322159,
 0.9999997101937759,
 0.9999997626066341,
 0.9999997628428897,
 0.9999997139316957,
 0.9999997577818901,
 0.999999755869811,
 0.9999997463605713,
 0.9999997364288542,
 0.9999997570609881,
 0.9999997448161363,
 0.9999997360467529,
 0.999999780259803,
 0.9999997598767889,
 0.9999997215929443,
 0.9999997127551777,
 0.9999997545192602,
 0.9999997260421248,
 0.9999997502976002,
 0.9999997570549642,
 0.9999997498782158,
 0.9999997536432763,
 0.9999997339043527,
 0.9999997327916236,
 0.9999997340323282,
 0.9999997520309855,
 0.9999997694492236,
 0.9999997212227125,
 0.9999997421704517,
 0.9999997500973927,
 0.9999997297544886,
 0.9999997205577663,
 0.9999997320294374,
 0.9999997381415552,
 0.999999733845299,
 0.9999997345495976,
 0.9999997412746235,
 0.9999997486291834,
 0.9999997448218729,
 0.9999997547194667,
 0.9999997500127386,
 0.9999997718534182,
 0.9999997617111425,
 0.9999997572094037,
 0.9999997259631819,
 0.9999997430010301,
 0.9999997226706518,
 0.9999997384556366,
 0.9999997451550446,
 0.99999976317977,
 0.9999997499005526,
 0.9999997314083571,
 0.9999997445608996,
 0.9999997684835801,
 0.9999997321768397,
 0.9999997352835809,
 0.9999997480695482,
 0.9999997482461893,
 0.9999997432505351,
 0.9999997220198347,
 0.9999997239909879,
 0.9999997552233533,
 0.9999997406902693]
```
What happened was the b vector was created by taking the dot product of the diagonally dominant matrix and a vector of ones.
Jacobi iteration was then used to see if the vector of ones could be recovered. As is seen above, Jacobi iteration did a good
job at recovering that vector.

**Implementation/Code:** The following is the code for jacobi(A, b, x0, tol, max_iter)
```python
from vec_err import err_2


def jacobi(A, b, x0, tol, max_iter):
    # Initialize variables needed for iterating
    n = len(b)
    r = [0 for i in range(len(b))]
    x1 = [0 for i in range(len(x0))]
    error = tol * 10.0
    iters = 0
    # Start iterating
    while error > tol and max_iter > iters:
        # Calculate the residual
        for i in range(n):
            r[i] = b[i]
            for j in range(n):
                r[i] += A[i][j] * x0[j]
        # Update the approximating vector
        for i in range(n):
            x1[i] = x0[i] - (r[i] / A[i][i])
        # Calculate l-2 error
        error = err_2(x0, x1)
        iters += 1
        # Create new x0 vector to continue iterating
        for i in range(n):
            x0[i] = x1[i]
    # Flip the sign
    x1 = [-1*x1[i] for i in range(len(x1))]
    # Return approximated solution
    return x1
```
**Last Modified:** December/2021

<hr>

[Previous](mat_prod.md)
| [Table of Contents](toc/manual_toc.md)
| [Next]()

<hr>
