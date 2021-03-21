import numpy as np

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

# Percentyle - wywołuje się podając zakres danych oraz procent wartości które mają być mniejsze lub równe
ages_percinteles = np.percentile(ages, 75)
print("Percentyl -", ages_percinteles)
# Oznacza że 75% liczb(z argumentu) jest mniejsze bądź równe 43.0