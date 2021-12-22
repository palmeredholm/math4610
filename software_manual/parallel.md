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

**Implementation/Code:** The following is the code for par_dot_prod()
```c
#include <stdio.h>
#include <omp.h>
#include <stdlib.h>

#define VECLEN 100
#define NUMTHREADS 8

void par_dot_prod(){
    int i, tid, len=VECLEN, threads=NUMTHREADS;
    double *a, *b;
    double sum, psum;

    printf("Starting omp_dotprod_openmp. Using %d threads\n", threads);

    a = (double*) malloc (len*threads*sizeof(double));
    b = (double*) malloc (len*threads*sizeof(double));

    for(i=0; i<len*threads; ++i){
        a[i] = 1.0;
        b[i] = a[i];
    }

    sum = 0.0;

#pragma omp parallel default(none) private(i,tid,psum) shared(sum, len, threads, a, b) num_threads(threads)
    {
        psum = 0.0;
        tid = omp_get_thread_num();

#pragma omp for reduction(+:sum)
        for(i=0; i<len*threads; i++){
            sum += (a[i] * b[i]);
            psum = sum;
        }
        printf("Thread %d partial sum = %f\n",tid, psum);
    }
    printf("Done. OpenMP version: sum  =  %f\n", sum);

    free (a);
    free (b);
}
```
**Last Modified:** December/2021

<hr>

[Previous](mat_norm_linf.md)
| [Table of Contents](toc/manual_toc.md)
| [Next]()

<hr>
