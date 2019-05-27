
SO_PATH <- "/Users/jlamb/repos/bedazzle/bazel-bin/src/lib/libadd_one.so"

.onLoad <- function(libname, pkgname){
    dyn.load(SO_PATH, local = FALSE)
}
