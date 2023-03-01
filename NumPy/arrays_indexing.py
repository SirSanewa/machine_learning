import numpy as np

arr = np.arange(0, 11)

print(arr[8])
print(arr[3:8])
print(arr[::2])
slice_arr = arr[:6]

# modifying slice of the array is still modifying original array
# to solve must create copy of array

arr_copy = arr.copy()

# indexing matrixes

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix[2][2])  # [row][column]
print(matrix[2, 2])  # (row, column) - recommended to use

# getting given columns from given rows
print(matrix[:2, -1])  # can use slices inside, get last item from 2 first rows
print(matrix[1:, :-1])

print(arr > 5)
bool_arr = arr > 5
print(arr[bool_arr])

print(arr[arr > 5])
