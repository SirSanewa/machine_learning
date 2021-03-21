import numpy as np

#  1 dimension
arr = np.array([1, 2, 3, 4])

print(arr[0])

#  2 dimension
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('5th element on 2nd dim: ', arr1[1, 4])

#  3 dimension
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr2[0, 1, 2])

#  negative indexing
arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('Last element from 2nd dim: ', arr3[1, -1])
