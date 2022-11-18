def quadrat(x):
    return x*x

lst = [1, 2, 3, 4, 5]
iterator = map(quadrat, lst)    # liefert einen Iterator
# entweder mit Schleife bearbeitet
'''
for i in iterator:
    print(i, end=' ')           # 1 4 9 16 25
'''
# oder in Liste verwandelt
liste = list(iterator)
print(liste)                    # [1, 4, 9, 16, 25]
# beides geht nicht - Iterator wird nur einmal durchlaufen
print()

# mittels Lambda
liste = list(map(lambda x: x**3, lst))
print(liste)                    # [1, 8, 27, 64, 125]

# List Comprehension
liste = [x**4 for x in lst]
print(liste)                    # [1, 16, 81, 256, 625]
