from ctypes import cdll, c_int, c_double, byref, POINTER, ARRAY, cast
import pkg_resources

lib = cdll.LoadLibrary(pkg_resources.resource_filename("bedazzle", "data/libadd_one.so"))

lib.add_one.restype = None
lib.add_one.argtypes = [POINTER(c_int)]


# >>> x = c_int(4)
# >>> x
# c_int(4)
# >>> bedazzle_lib.lib.add_one(byref(x))
# >>> x
# c_int(5)

lib.linreg.restype = None
lib.linreg.argtypes = [POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

def linreg(x, y):
    x_array = (c_double * len(x))(*x)
    y_array = (c_double * len(y))(*y)

    m = c_double(0)
    b = c_double(0)
    lib.linreg(byref(c_int(len(x))),
               cast(x_array, POINTER(c_double)), 
               cast(y_array, POINTER(c_double)),
               byref(m),
               byref(b))
    return (m, b)
