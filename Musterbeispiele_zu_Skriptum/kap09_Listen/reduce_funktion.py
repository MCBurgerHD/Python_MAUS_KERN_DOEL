from functools import reduce

lst = list(range(1, 11))
print(lst)          # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wert = reduce(lambda x, y: x + y, lst)  # entspricht der Funktion summe
print(wert)
