import eingabe

def ggT(a, b):
    while a != b:
        while a > b:
            a = a - b
        while b > a:
            b = b - a
    return b

def ggT2(a, b):
    rest = a % b
    while rest > 0:
        a = b
        b = rest
        rest = a % b
    return b


zahl1 = int(input("Zahl 1 : "))
zahl2 = int(input("Zahl 2 : "))

teiler = ggT(zahl1, zahl2)
teiler2 = ggT2(zahl1, zahl2)
print("ggT : ",teiler)
print("ggT2 : ",teiler2)