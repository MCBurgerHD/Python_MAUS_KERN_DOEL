def sieben_zahlen():
    a = 0
    ziffer = "7"
    for f in range(1000, 10000):
        a += count_digits(str(f), ziffer)
    return a

def count_digits(ganze_zahl, ziffer):
    zähler = 0
    for i in ganze_zahl:
        if i == ziffer:
            zähler += 1
    return zähler

ganze_zahl = input("Zahl : ")
ziffer = input("Ziffer : ")
zähler = count_digits(ganze_zahl, ziffer)
print("Anzahl der Ziffer : ", zaehler)

print("Die Zahl kommt", sieben_zahlen(), "in vierstelligen Zahlen vor." )