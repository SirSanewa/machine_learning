import numpy as np

# one dimensional array
my_list = [1, 2, 3]
a = np.array(my_list)
print(type(a))
print(a)

# multi dimensional array
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = np.array(my_matrix)
print(type(b))
print(b)

# generate array
new = np.arange(0, 11, 2)
print(type(new))
print(new)

# generate array with only zeros or ones
print(np.zeros((3, 3)))
print(np.ones((2, 4)))

# generate random array of decimals
print(np.random.rand(5))

# generate random array of decimals with minus as well
print(np.random.randn(2, 3))

# generate random array of integers (low, max, amount)
print(np.random.randint(1, 11, 5))
