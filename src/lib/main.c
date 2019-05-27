
# include "add_one.c"
# include "linreg.c"

int main()
{
    int n = 6;
    REAL x[6]= {1, 2, 4,  5,  10, 20};
    REAL y[6]= {4, 6, 12, 15, 34, 68};

    REAL m,b,r;
    linreg(n,x,y,&m,&b,&r);
    printf("m=%g b=%g r=%g\n",m,b,r);
    return 0;
}
