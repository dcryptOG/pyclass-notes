#floats and integers
import numpy as np
x = np.random.random(10)
print(x)
# [ 0.07837821  0.48002108  0.41274116  0.82993414  0.77610352  0.1023732
#   0.51303098  0.4617183   0.33487207  0.71162095]

np.set_printoptions(precision=3)
print(x)
# [ 0.078  0.48   0.413  0.83   0.776  0.102  0.513  0.462  0.335  0.712]
# PYTHON ONLY ACCURATE FOR 53 BITS,
