def f1():
    y = 5
    print(x)
    print(y)

def f2():
    z = 5
    print(z)

x = 3
f1()
# print(y)    geht nicht -> kein y

z = 3
f2()        #  Ausgabe 5 - lokales z der Fkt
print(z)    #  Ausgabe 3 - global z