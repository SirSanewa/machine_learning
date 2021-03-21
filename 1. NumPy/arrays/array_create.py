import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr_tupple = np.array((1, 2, 3, 4, 5))

lisy = [1, 2, 3, 4, 5]

# print(arr)
# print(arr_tupple)
# print(lisy)

#  0D array
np.array(42)

#  1D array
np.array([1, 2, 3, 4, 5])

#  2D array
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr1)

#  3D array
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr2)

#  get number of dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

#  higher dimensions
arr3 = np.array([1, 2, 3, 4], ndmin=5)

print(arr3)
print('number of dimensions :', arr3.ndim)
