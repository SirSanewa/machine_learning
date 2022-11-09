import numpy as np

arr = np.arange(1, 26)
random_arr = np.random.randint(0, 101, 10)

print(arr, random_arr, sep="\n")

# Reshape array to multidimensional
reshaped_array = arr.reshape(5, 5)
print(reshaped_array)

# return max and min value
print(random_arr.max())
print(random_arr.min())

# index of max and min value
print(random_arr.argmax())
print(random_arr.argmin())

# get shape of an array
# for one dimensional array result will be tuple with one number f.e. (25,)
print(arr.shape)
print(reshaped_array.shape)

# type of data inside array
print(arr.dtype)
