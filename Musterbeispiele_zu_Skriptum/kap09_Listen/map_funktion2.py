def sum(x, y):
    return x + y

lst1 = [1, 3, 5]
lst2 = [9, 8, 12, 13]

lstNeu = list(map(sum, lst1, lst2))
print(lstNeu)                       # [10, 11, 17]
