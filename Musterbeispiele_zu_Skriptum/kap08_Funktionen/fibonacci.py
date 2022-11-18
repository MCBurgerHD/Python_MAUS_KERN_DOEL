#!/usr/bin/env python3
# herkömmliche Funktion, liefert die ersten n Fibonacci-Zahlen
def fiblst(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result += [a]
        a, b = b, a+b
    return result

print(fiblst(10))     
# Ausgabe [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Generator-Funktion
def fibgen(n):
    cnt = 0
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b
        cnt += 1
        if cnt > n:
            return

print(fibgen(10))   # erzeugt nur das Generator-Objekt nicht die Liste!
# Ausgabe <generator object fibgen at 0x01148FB0>

generator = fibgen(10)
for i in generator:        # über generierte Liste abgearbeitet
    print(i, end = ' ')
print()
#  alle Werte wurden durchlaufen Liste ist leer!
print(list(generator))

print(list(fibgen(10)))     # erneute Erzeugung eines Generators und in Liste verwandelt
# Ausgabe [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Fibonacci-Zahlen < 1000 ausgeben
gen = fibgen(100)		# Erzeugt das Generatorobjekt
fib = next(gen)		# mittels next wird 1.Element geliefert
while fib<1000:		# solange diese <1000
    print(fib, end=' ')	# Ausgabe
    fib = next(gen)		# nächstes Element abholen
# Ausgabe: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
print()

# nochmals, aber Generator zu klein
gen = fibgen(10)
fib = next(gen)
while fib<1000:
    print(fib, end=' ')
    fib = next(gen, None)
    if fib == None: 
        print('Generator erschöpft')
        break
print()
