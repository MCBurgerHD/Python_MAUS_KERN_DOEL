import random, math

a = 0.7
b = 0.9
c = a + 0.1
d = b - 0.1
print(c == d)   # Dezimalwerte sind ungenau
print(abs(c-d) < 1e-6)
print(c - d)

print(math.sqrt(2))		# Wurzel aus 2 -> 1.4142135623730951
print(math.sin(0.4))	# 0.3894183423086505

# Erzeugung von Zufallszahlen (dezimal)
print(random.random())      # Wert zwischen 0 und 1 [0;1[
print(random.uniform(3.2, 7.5))     # Wert zwischen a und b [a; b) ob b hängt von Rundung ab

