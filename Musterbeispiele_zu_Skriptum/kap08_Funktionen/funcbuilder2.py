#!/usr/bin/env python3
import math

def verschachteln(f, g, x):
    return f(g(x))
  
# Anwendung
verschachteln(print, math.sqrt, 2)         # 1.4142135623730951
print(math.sqrt(2))                        # 1.4142135623730951

print(verschachteln(math.sqrt, abs, -4))    # 2.0  
ergebnis = verschachteln(math.sin, math.sqrt, 0.5)
print(ergebnis == math.sin(math.sqrt(0.5)))  # True
  