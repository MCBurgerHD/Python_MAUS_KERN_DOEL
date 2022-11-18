def gerade_ungerade(zahl):
    gerade = 0
    ungerade = 0
    while zahl:
        letzesglied = zahl % 10
        zahl = zahl // 10
        if letzesglied % 2 == 0:
            gerade += 1
        elif letzesglied % 2 == 1:
            ungerade += 1
    return gerade, ungerade

zahl = int(input("Zahl : "))

ausgabe = gerade_ungerade(zahl)

print(ausgabe)