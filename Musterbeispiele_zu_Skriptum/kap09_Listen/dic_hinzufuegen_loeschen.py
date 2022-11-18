# Erzeugung eines Dic. über Comprehension
d = {k:chr(k + 65) for k in range(5)}
print(d)        # {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
print(len(d))   # Länge 5

d[5] = 'G'      # hinzugefügt - weil Schlüssel noch nicht vorhanden
print(d)        # {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'G'}
print(len(d))   # Länge 6
d[5] = 'F'      # Value von Schlüssel ersetzt
print(d)        # {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}

x = d.setdefault(6, 'G')    # fügt Schlüssel-Werte Paar hinzu
print(x, ' - ', d)          # rückgeliefert wurde der neu hinzugefügte Wert
# G  -  {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G'}
x = d.setdefault(6, 'A')    # ändert nichts
print(x, ' - ', d)          # rückgeliefert wurde der bereits vorhandene Wert
# G  -  {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G'}

del d[3]        # Löscht Paar mit Schlüssel 3
print(d)        # {0: 'A', 1: 'B', 2: 'C', 4: 'E', 5: 'F', 6: 'G'}
try:
    del d[3]    # erzeugt KeyError weil Schlüssel 3 nicht vorhanden
except KeyError:
    print('Element bereits gelöscht')

print(d.keys())         # dict_keys([0, 1, 2, 4, 5, 6])
print(d.values())       # dict_values(['A', 'B', 'C', 'E', 'F', 'G'])
s = set(d.keys())       # Umwandlung in Set
print(s)                # {0, 1, 2, 4, 5, 6}
l = list(d.values())    # Umwandlung in List
print(l)                # ['A', 'B', 'C', 'E', 'F', 'G']