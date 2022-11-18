def f(n):
    if isinstance(n, int):
        return 2+n
    else:
        print("Ungültiger Parameter")
        return -1

print(f(3))                 # Ausgabe 5
print(f('asdf'))            # Ausgabe Ungültiger Parameter  und  -1
a="27fgASDdhfg"
print(f(a))

def g(n: int) -> int:
    return 2*n

print(g(2))             # Ausgabe 4 (richtige Benutzung)
print(g('abc'))         # Ausgabe abcabc (nicht typkonform - aber hier möglich)
