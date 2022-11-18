lst1 = [1, 2, 3, 9, 345, 36, 5, 8, 33]

# in lst2 sollen alle durch 3 teilbaren Zahlen von lst1
lst2 = list(filter(lambda x: x%3 == 0, lst1))
print(lst2)     # [3, 9, 345, 36, 33]

# alle Elemente durch 3 dividieren
lst3 = list(map(lambda x: x//3, lst1))
print(lst3)     # [0, 0, 1, 3, 115, 12, 1, 2, 11]

def f1(x, y):
    return (x+1) * (y+1)

# gleichwertiger Lambda-Ausdruck
f2 = lambda x, y: (x+1) * (y+1)

print(f1(2, 3))           # 12
print(f2(2, 3))           # 12
