# bedazzle

We tried to learn how to build a C++ project in Bazel and then do other stuff with it.

## Setup

### On Mac 
#### Install bazel

If you don't have `bazel` yet, install it (per [these instructions](https://docs.bazel.build/versions/master/install-os-x.html#install-with-installer-mac-os-x)).

```
BAZEL_VERSION=0.22.0
BAZEL_INSTALLER=https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-installer-darwin-x86_64.sh

# Checksums are for nerds
wget ${BAZEL_INSTALLER} -O bazel.sh

# Install it
chmod +x bazel.sh
./bazel.sh --user
```

Manually update your path in `~/.bash-profile`, adding `${HOME}/bin`.

#### Install gcc

If you don't have `gcc` yet, install it.

## Building the project

From the repo root, run

```
bazel build //src/lib:libadd_one.so
```

Set this up so you don't have to do that dumb thing

```
alias bazel-deps="bazel query --nohost_deps --noimplicit_deps 'deps(//main:hello-world)' --output graph"
```

## Using Python

### Installation
`python setup.py develop`

Example:
```
 [01:13:42] $ python
Python 3.5.2 |Anaconda custom (x86_64)| (default, Jul  2 2016, 17:52:12)
[GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from bedazzle import lib as bdlib
>>> from ctypes import c_int, byref
>>> my_int = c_int(9000)
>>> bdlib.add_one(my_int)
>>> my_int
c_int(9001)
```

## Using R

Build by running `./build_r.sh`

Then, in R:

```{r}
library(bedazzle)

# should print 11
bedazzle::add_one(10)
```

## References

* [bazel workspaces](https://docs.bazel.build/versions/master/build-ref.html#workspaces)
* [building a C++ project in bazel](https://docs.bazel.build/versions/master/tutorial/cpp.html)
* [extending Python with C++](https://docs.python.org/3/extending/extending.html)
* [extending R with C++](https://www.r-bloggers.com/three-ways-to-call-cc-from-r/)
