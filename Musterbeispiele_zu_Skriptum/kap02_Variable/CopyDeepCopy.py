import copy

x = [1, 2, 3]
y = copy.copy(x)
print(x, y)
x[1] = 1000
print(x, y)

# allerdings
a = [1, 2, [3, 4]]
b = copy.copy(a)
print(a, b)
a[2][1] = 1000  
'''  ändert beide - weil Element 2 ist veränderbar
     man verweist nur auf das Objekt
     somit wird dieses Objekt verändert
     es handelt sich nur um eine Kopie der obersten
     und nicht aller Ebenen '''
print(a, b)
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)
print(a, b)
a[2][1] = 1000
# Kopie auf allen Ebenen
print(a, b)
