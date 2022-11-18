import eingabe
def kgV(a,b):
    x = ggT(a,b)
    y = (a*b)/x
    return y

def ggT(a, b):
    rest = a % b
    while rest > 0:
        a = b
        b = rest
        rest = a % b
    return b

zahl1 = int(input("Zahl 1 : "))
zahl2 = int(input("Zahl 2 : "))


kgV = kgV(zahl1, zahl2)
print(int(kgV))