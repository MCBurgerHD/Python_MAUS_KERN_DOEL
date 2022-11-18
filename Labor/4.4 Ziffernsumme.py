def ziffernsumme(zahl):
    a = 0
    while zahl:
        a += zahl % 10
        zahl = int(zahl / 10)
    return a
    print(a)
i = 10000
b = 0
while i <= 100000:
    if ziffernsumme(i) == 10:
        b +=1
    i += 1
print(b)