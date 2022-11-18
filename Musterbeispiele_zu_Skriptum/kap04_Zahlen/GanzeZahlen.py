import sys
import random
from random import randint

x = 2**100
print(x)
print(sys.maxsize)  # größte direkte Ganzzahl -> 2^63-1
# print(2/0)    bewirkt ZeroDivisionError: division by zero

print(0xa0)     # hexadezimal 160
x = 165
print(hex(x))   # hex, binär oder oktal
print(bin(x))
print(oct(x))
print(0b10001)  # Ganzzahl nicht dekadisch
print(0o245)

# Zufallszahlen
print(randint(1, 6))    # Ganzzahl [a; b] beide Grenzen inklusiv
print(random.randrange(1, 2))       # Wert zwischen a und exkl. b [a;b[
print(random.randrange(2))          # nur Endwert [0; b[
print(random.randrange(1, 10, 2))   # (ev. mit Schrittweite c)
