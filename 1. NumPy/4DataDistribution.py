import numpy as np
from scipy import stats
# To create array of 250 random floats between 0 and 5
x = np.random.uniform(0.0, 5.0, 250)

print(x)
print(np.mean(x))
print(np.median(x))
print(stats.mode(x))
print(np.std(x))
