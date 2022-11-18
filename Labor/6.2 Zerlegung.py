#----------------------------------------------------------------
# Maximilian Ertl
# 27.5.2021
#                           zerlegung
# Bstimmt welche und wie viele Primzahlen in der uebergebenen
# Zahl enthalten sind
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#                           zerlegung
# Zerlegt die Zahl in die Anzahl ihrer Primzahlen und fuegt diese
# in ein Dictionary
#-----------------------------------------------------------------


def zerlegung(zahl):
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
    dictionary = {}
    for teiler in strplist:
        if teiler in dictionary:
            dictionary[teiler] += 1
        else:
            dictionary[teiler] = 1
    return dictionary


zahl = int(input("Zahl : "))
print(zerlegung(zahl))