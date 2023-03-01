import numpy as np

#  Create array of 10 zeros
arr_zeros = np.zeros(10)
print(arr_zeros)

#  Create an array of 10 ones
arr_ones = np.ones(10)
print(arr_ones)

#  Create an array of 10 fives
arr_fives = np.zeros(10) + 5
print(arr_fives)

#  Create an array of the integers from 10 to 50
arr_10_50 = np.arange(10, 51)
print(arr_10_50)

#  Create an array of all even integers from 10 to 50
arr_even_10_50 = np.arange(10, 51, 2)
print(arr_even_10_50)

#  Create a 3x3 matrix with values from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print(matrix_3x3)

#  Create identity matrix 3x3
print(np.eye(3))

#  Generate random number between 0 and 1
print(np.random.rand(1))

#  Generate an array of 25 random numbers from a standard normal distribution
print(np.random.randn(25))

#  Create a 10x10 matrix with decimal numers in order
matrix_10x10 = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
print(matrix_10x10)
#  other solution
print(np.linspace(0.01, 1, 100).reshape(10, 10))

#  Create an array of 20 linearly spaced points between 0 and 1
print(np.linspace(0, 1, 20))

#  Create primary array of:
# [[ 1  2  3  4  5]
# [ 6  7  8  9 10]
# [11 12 13 14 15]
# [16 17 18 19 20]
# [21 22 23 24 25]]

mat = np.arange(1, 26).reshape(5, 5)

#  Get only:
# [[12 13 14 15]
#  [17 18 19 20]
#  [22 23 24 25]]
print(mat[2:, 1:])

#  Get only:
#  [20]
print(mat[3, -1])

# Get only:
# [[2],
# [7],
# [12]]
print(mat[:3, 1:2])

#  Get only:
#  [21 22 23 24 25]
print(mat[-1])

#  Get only:
#  [[16 17 18 19 20]
#  [21 22 23 24 25]]
print(mat[-2:])

#  Get sum of primaty matrix
print(np.sum(mat))

#  Get the standard deviation of values in mat
print(np.std(mat))

#  Get the sum of columns
print(mat.sum(axis=0))
