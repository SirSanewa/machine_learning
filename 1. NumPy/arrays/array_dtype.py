import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr1 = np.array(['apple', 'banana', 'cherry'])
print(arr1.dtype)

#  create array with predefined values type
arr2 = np.array([1, 2, 3, 4], dtype='S')
print(arr2)
print(arr2.dtype)

#  create array with predefined values type and byte values 4
arr4 = np.array([1, 2, 3, 4], dtype='i4')
print(arr4)
print(arr4.dtype)

#  convert data type on existing array
arr5 = np.array([1.1, 2.1, 3.1, 4.99])
newarr = arr5.astype('i')
print(newarr)
print(newarr.dtype)

arr6 = np.array([1.1, 2.1, 3.1])
newarr2 = arr6.astype(int)
print(newarr2)
print(newarr2.dtype)
