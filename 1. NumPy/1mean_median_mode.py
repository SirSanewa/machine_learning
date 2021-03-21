import numpy
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Średnia
speed_mean = numpy.mean(speed)
print("Średnia -", speed_mean)

# Mediana
speed_median = numpy.median(speed)
print("Mediana -", speed_median)

# Najczęściej występująca wartość, zwraca ModeResult(mode=array([jaka wartość]), count=array([ile razy]))
speed_mode = stats.mode(speed)
print("Najczęściej występuje -", speed_mode)
print("Najszęsciej występuje liczba:", *speed_mode[0])
print("Ilość razy:", *speed_mode[1])




