lst = list(range(10, 101, 10))
print(lst)          # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print('Anzahl der Elemente', len(lst))     # Anzahl der Elemente 10
lst.insert(5, 55)       # fügt an Indexposition 5 den Wert 55 hinzu
print(lst)              # [10, 20, 30, 40, 50, 55, 60, 70, 80, 90, 100]

wert = lst.pop(10)      # entfernt das Indexelement 10 und liefert es zurück
print(wert)             # 100
print(lst)              # [10, 20, 30, 40, 50, 55, 60, 70, 80, 90]

lst.extend([101, 102, 103])         # fügt an die Liste eine weitere hinzu
print(lst)          # [10, 20, 30, 40, 50, 55, 60, 70, 80, 90, 101, 102, 103]

lst = list(range(10, 51, 10))   # neue Liste
print(lst)              # [10, 20, 30, 40, 50]
lst += lst              # # fügt an die Liste die selbe hinzu
# entspricht lst.extend(lst)
print(lst)              # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

del lst[3]             # löscht Element mit Index 3
print(lst)              # [10, 20, 30, 50, 10, 20, 30, 40, 50]
del lst[0:4]            # löscht die ersten 4 Elemente
print(lst)              # [10, 20, 30, 40, 50]
del lst[-3: ]           # löscht die letzten 3 Elemente
print(lst)              # [10, 20]
lst.remove(10)          # entfernt Element mit Wert 10
print(lst)              # [20]
# lst.remove(10) bewirkt ValueError weil Element mit Wert 10 nicht vorhanden
