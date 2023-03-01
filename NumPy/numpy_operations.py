import numpy as np


arr = np.arange(0, 11)

#  ALL UNIVERSAL FUNCTIONS CAN BE FIND IN SCIPY>ORG "UFUNC"

#  will add same index values together not appending the array (same for all mathematical operations)
print(arr + arr)

#  will add 100 to every value in the array
print(arr + 100)

#  do potęgi
print(arr ** 2)

#  square root - pierwiastek
print(np.sqrt(arr))

#  exponential - wykładnia
print(np.exp(arr))

#  maximal value (or can be done via arr.max())
print(np.max(arr))
