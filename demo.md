

# Build the project

```
bazel build //src/lib:libadd_one.so
```

# Try it in R!

```{r}
library(bedazzle)

X <- as.double(rnorm(100))
Y <- as.double(rnorm(100))

reg <- bedazzle::linreg(X, Y)

summary(lm(Y ~ X))
```

## Try it in python!

```{python}
import numpy as np
import bedazzle

X = np.random.uniform(size=100)
Y = np.random.uniform(size=100)
bedazzle.linreg(X,Y)

```
