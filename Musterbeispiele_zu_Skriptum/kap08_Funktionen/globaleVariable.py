'''
z = 3

def f1():
    z = z + 3  # geht nicht - z lokal -> nicht initialisiert!
    print(z)

f1()
'''

def f1():
    global z
    z = z + 3  # geht weil - z global ->  initialisiert!
    print(z)

z = 3
f1()        #  Ausgabe 6

print()

# besser

def f2(x):
    return x + 3

def f3(x):
    x = x+3

x = 3

f3(x)
print(x)

z = f2(x)
print(x)
print(z)
