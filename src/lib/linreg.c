#include <stdio.h>

// Linear regression
// Ref: https://stackoverflow.com/a/19040841
#include <stdlib.h>
#include <math.h>                           /* math functions */

//#define REAL float
#define REAL double

inline static REAL sqr(REAL x) {
    return x*x;
}

/*
n = number of data points
x,y  = arrays of data
*b = output intercept
*m  = output slope
*/
void linreg(int *n, REAL *x, REAL *y, REAL *m, REAL *b){
    
    double sumx;
    double sumxsq;
    double sumy;
    double sumxy;
    double denom;

    // capture the sum of squares as we go
    sumx = 0;
    sumxsq = 0;
    sumy = 0;
    sumxy = 0;

    // Loop over rows
    for(int i = 0; i < *n; i++){
      sumx += x[i];
      sumxsq += pow(x[i], 2);
      sumy += y[i];
      sumxy += x[i] * y[i];
    }

    denom = *n * sumxsq - pow(sumx, 2);

    // intercept
    *b = (sumy * sumxsq - sumx * sumxy) / denom;

    // slope
    *m = (*n * sumxy - sumx * sumy) / denom;
}
