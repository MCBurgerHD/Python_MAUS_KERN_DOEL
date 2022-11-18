def datum_ein():
    datum = input("Geben Sie ein Datum (TT.MM.JJJJ) in : ")
    try:
        tag, monat, jahr = datum.split(".")
        tag = int(tag)
        monat = int(monat)
        jahr = int(jahr)
    except:
        return 0,0,0
    return tag, monat, jahr

t, m, j = datum_ein()

if t == 0:
    print("Fehler")
else:
    print(t , "." , m , "." , j)