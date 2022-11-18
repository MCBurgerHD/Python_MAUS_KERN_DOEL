lst = list(range(10, 51, 10))   # neue Liste
print(lst)              # [10, 20, 30, 40, 50]

lst.append(10)          # fügt weiteres Element hinten dran
print(lst)              # [10, 20, 30, 40, 50, 10]
anzahl = lst.count(10)  # wieoft kommt der Wert 10 vor
print(anzahl)           # 2
n = lst.index(10)       # liefert 1.Auftreten von Wert 10
print(n)                # 0
n = lst.index(10, 1, len(lst))   # liefert 1.Auftreten von Wert 10 ab Index 1
print(n)                # 5
# lst.index(5) erzeugt einen ValueError weil 5 nicht vorkommt
print(5 in lst)         # False
print(10 in lst)        # True
print(5 not in lst)     # True
print(10 not in lst)    # False

klein = min(lst)        # liefert kleinsten Wert
gross = max(lst)        # liefert größten Wert
print(klein, gross)     # 10 50

lst.clear()             # löscht die Liste
print(lst)              # []

lst = list(range(10, 51, 10))   # neue Liste
print(lst)              # [10, 20, 30, 40, 50]
lst.reverse()
print(lst)              # [50, 40, 30, 20, 10]

summe = sum(lst)        # Summiert die Werte
print(summe)            # 150
summe = sum(lst, 33)    # Summiert die Werte und gibt Ausgang 33 hinzu
print(summe)            # 183

lst[1] = 3              # wert von Index 1 wird auf 3 gesetzt
print(lst)              # [50, 3, 30, 20, 10]

lst.sort()              # sortiert in aufsteigender Form
print(lst)              # [3, 10, 20, 30, 50]

lst2 = list(range(50, 9, -10))   # neue Liste
print(lst2)             # [50, 40, 30, 20, 10]
lst[2:4] = lst2         # Werte zwischen Index 2 bis 4 (exkl.) werden durch lst2 ersetzt
print(lst)              # [3, 10, 50, 40, 30, 20, 10, 50]
