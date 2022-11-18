zahl = int(input("positive Ganzzahl : "))

if zahl < 0:
    exit()
pzahl = 2
plist = []
while zahl != 1:
    if zahl % pzahl == 0:
        plist.append(pzahl)
        zahl = zahl // pzahl
    else:
        pzahl += 1
strplist = [str(int) for int in plist]
sep = " * "
print(sep.join(strplist))