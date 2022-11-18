s = {2, 3, 4, 1, 5, 24, 31, 17}
print(s)                # {1, 2, 3, 4, 5, 17, 24, 31}

s.add(3)                # Duplikat - nicht hinzugefügt
s.add(19)               # hinzugefügt
print(s)                # {1, 2, 3, 4, 5, 17, 19, 24, 31}

s.remove(3)
print(s)                # {1, 2, 4, 5, 17, 19, 24, 31}
try:
    s.remove(3)         # Erzeugt Fehler - nicht mehr vorhanden
except Exception:
    print("Element nicht im Set!")

s.discard(3)
print(s)                # {1, 2, 4, 5, 17, 19, 24, 31}
print(3 in s)           # False
print(5 in s)           # True
s.clear()               # löscht Set
print(s)                # set() -> {}
s.add('A')
print(s)                # {'A'}
