#!/usr/bin/env python3
import math

def buildlist(n, start, end, fn):
    liste = []
    if n<=1:
      return liste                    # leeres Ergebnis
    delta = (end - start) / (n-1)     # Schrittweite
#    return [ fn(start + i*delta) for i in range(n)]  # List-Comprehension
    for i in range(n):
      liste.append(fn(start + i*delta))
    return liste

# Anwendung
lst1 = buildlist(5, 0.0, 4.0, math.sqrt)
print(lst1)

lst2 = buildlist(9, 0.0, 2.0, lambda x: x)
print(lst2)
