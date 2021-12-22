# Parallelism

**Routine Name:** par_dot_prod

**Author:** Palmer Edholm

**Language:** C.

**Description/Purpose:** These routines show how previous routines in this software manual can be optimized using parallel
programming techniques.

**Input (par_dot_prod):** There are no inputs needed in this case. Even though there are arguments supplied, the real purpose is to
return values in those variables.

**Output:** This routine returns a scalar that is the dot product of two very long, conformable vectors.

**Usage/Example:**

The laptop I'm using has eight processors, so the could below is written to optimize my specific computer. This code is
based off of the code written by Xavier Besseron: https://gitlab.uni.lu/SC-Camp/2018/Parallel_Programming_Models/blob/f25ef077865b1e7ad9142c4d42ec5a00ff973edb/examples/OpenMP/dotProduct/dotProductOpenMP.c.
```c
#include "par_dot_prod.h"

int main(int argc, char* argv[]) {
    par_dot_prod();
    return 0;
}
```
Output from the lines above:

      24   5.96046448E-08

The first value (24) is the number of binary digits that define the machine epsilon and the second is related to the
decimal version of the same value. The number of decimal digits that can be represented is roughly eight (E-08 on the
end of the second value).

**Implementation/Code:** The following is the code for smaceps()

      subroutine smaceps(seps, ipow)
    c
    c set up storage for the algorithm
    c --------------------------------
    c
          real seps, one, appone
    c
    c initialize variables to compute the machine value near 1.0
    c ----------------------------------------------------------
    c
          one = 1.0
          seps = 1.0
          appone = one + seps
    c
    c loop, dividing by 2 each time to determine when the difference between one and
    c the approximation is zero in single precision
    c --------------------------------------------- 
    c
          ipow = 0
          do 1 i=1,1000
             ipow = ipow + 1
    c
    c update the perturbation and compute the approximation to one
    c ------------------------------------------------------------
    c
            seps = seps / 2
            appone = one + seps
    c
    c do the comparison and if small enough, break out of the loop and return
    c control to the calling code
    c ---------------------------
    c
            if(abs(appone-one) .eq. 0.0) return
    c
        1 continue
    c
    c if the code gets to this point, there is a bit of trouble
    c ---------------------------------------------------------
    c
          print *,"The loop limit has been exceeded"
    c
    c done
    c ----
    c
          return
    end

**Last Modified:** December/2021

<hr>

[Previous](mat_norm_linf.md)
| [Table of Contents](toc/manual_toc.md)
| [Next]()

<hr>
