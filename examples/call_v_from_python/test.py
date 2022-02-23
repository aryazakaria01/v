from ctypes import *
import math, os

so_file = "./test.dll" if os.name=="nt" else "./test.so"
lib = CDLL(so_file)
assert lib.square(10) == 100, "Cannot validate V square()."

lib.sqrt_of_sum_of_squares.restype = c_double
assert lib.sqrt_of_sum_of_squares(c_double(1.1), c_double(2.2)) == math.sqrt(1.1*1.1 + 2.2*2.2), "Cannot validate V sqrt_of_sum_of_squares()."
