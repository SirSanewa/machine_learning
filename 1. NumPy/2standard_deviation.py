import numpy as np

speed = [86, 87, 88, 86, 87, 85, 86]

speed_mean = np.mean(speed)
print("Średnia -", speed_mean)

# Odchylenie Standardowe
speed_deviation = np.std(speed)
print("Odchylenie standardowe - ", speed_deviation)
print("")
speed2 = [32, 111, 138, 28, 59, 77, 97]

speed_mean2 = np.mean(speed2)
print("Średnia -", speed_mean2)

speed_deviation2 = np.std(speed2)
print("Odchylenie standardowe - ", speed_deviation2)

# Wariacja
speed_variance = np.var(speed2)
print("Wariacja - ", speed_variance)
