import math
def ist_datum_gülig(tag, monat, jahr):
    if tag > 29 and monat == 4 and sjahr == True:
        print("Fehler")
    elif tag > 31:
        print("Fehler")
    elif tag > 30 and monat == [2, 4, 6, 9, 11]:
        print("Fehler")
    elif tag < 1 and monat < 1:
        print("Fehler")
    return tag

def ist_schaltjahr(jahr):
    if math.fmod(jahr,400)==0:
        a = True
    elif math.fmod(jahr,100)==0:
        a = False
    elif math.fmod(jahr,4)==0:
        a = True
    return a

def gib_maximal_tag(monat, jahr):
    if sjahr == True and monat == 2:
        tage = 29
    elif sjahr == False and monat == 2:
        tage = 28
    elif monat == [1, 3, 5, 7, 8, 10, 12]:
        tage = 31
    else:
        tage = 30
    return tage

tag = int(input("Tag : "))
monat = int(input("Monat : "))
jahr = int(input("Jahr : "))

datum = ist_datum_gülig(tag, monat, jahr)
sjahr = ist_schaltjahr(jahr)
mtage = gib_maximal_tag(monat, tag)

if tag == 31 and monat == 1 or 3 or 5 or 7 or 8 or 10 or 13:
    ndatum = monat+1
    print("Morgiges datum : 1" , ndatum , jahr)
elif tag == 30 and monat == 4 or 6 or 9 or 11:
    ndatum = monat+1
    print("Morgiges Datum : 1", ndatum, jahr)
elif tag >= 29 and monat == 2:
    ndatum = monat+1
    print("Morgiges datum : 1", ndatum, jahr)


print(datum)
print(mtage)
print(sjahr)