def teilbar_2(x):
    return x%2 == 0

lst = list(range(1, 11))
print(lst)          # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# mit 'normaler' Funktion
ergebnis = filter(teilbar_2, lst)   # Iterator mit nur mehr geraden Zahlen
print(list(ergebnis))               # [2, 4, 6, 8, 10]  als Liste
# Ursprungsliste wird nicht verändert!
print(lst)          # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# mit Lambda-Funktion
ergebnis = filter(lambda x: x%2 != 0, lst)   # Iterator mit nur mehr ungeraden Zahlen
print(list(ergebnis))               # [1, 3, 5, 7, 9]  als Liste
# Ursprungsliste wird nicht verändert!
print(lst)          # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# mit List-Comprehension
print([x for x in lst if x%2 == 0]) # [2, 4, 6, 8, 10]
