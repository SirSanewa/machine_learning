import matplotlib.pyplot as plt


x = [i for i in range(10)]
y = [i*2 for i in x]

# create plot graph with x and y lists
# plt.plot(x, y)

# create scattered points graph with x and y lists
plt.scatter(x, y)

# label names
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# show graph
plt.show()
