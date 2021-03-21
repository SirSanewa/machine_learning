import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 5.0, 100)

plt.hist(x, 5) # liczba wykresów słupkowych
plt.show()
# pokazuje, że między 0 a 1 jest 14 wartości
