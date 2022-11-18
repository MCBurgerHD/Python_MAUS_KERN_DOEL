#!/usr/bin/env python3
import math

def funcbuilder(f, n):
  def newfunc(x): 
      return f(n*x)  # Ergebnis von newfunc
  return newfunc     # Ergebnis von funcbuilder

# bildet die Funktion sin(2*x)
f1 = funcbuilder(math.sin, 2)
print(f1(0.4), math.sin(0.4*2))
# Ausgabe 0.7173560908995228 0.7173560908995228

# bildet die Funktion sqrt(4*x) - Wurzel(4*x)
f2 = funcbuilder(math.sqrt, 4)
print(f2(1), math.sqrt(1*4))
# Ausgabe 2.0  2.0

def funcbuilderL(f, n):
    return lambda x: f(n*x)

f3 = funcbuilderL(abs, 3)           # Absolutbetrag 3*x
print(f3(-2.1))                     # 6.300000000000001
print(funcbuilderL(abs, 3)(-2.3))   # 6.8999999999999995
