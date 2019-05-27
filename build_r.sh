#!/bin/bash

set -e

# Build the C++ target object
# TODO: These flags are bad and they're used
#       to skirt around a deprecation error
bazel build //src/lib:libadd_one.so \
    --incompatible_remove_native_git_repository=false \
    --incompatible_remove_native_http_archive=false

pushd r-pkg/
    Rscript -e "devtools::document()"
    R CMD INSTALL .

    Rscript -e "print(bedazzle::add_one(10))"
    Rscript -e "set.seed(123); X <- as.double(rnorm(1000)); Y <- as.double(rnorm(1000)); bedazzle::linreg(X, Y)"
popd
