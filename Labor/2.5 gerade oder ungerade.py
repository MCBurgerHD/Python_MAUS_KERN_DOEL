zahl = input("Zahl : ")
try:
    zahl = int(zahl)
    if zahl % 2:
        print("Die Zahl ist ungerade.")
        if zahl>0:
            print("Die Zahl ist positiv.")
        else:
            print("Die Zahl ist negativ")
    else:
        print("Die Zahl ist gerade.")
        if zahl>0:
            print("Die Zahl ist positiv.")
        else:
            print("Die Zahl ist negativ")
except ValueError:
    print("Fehler. Erwartet war eine Zahl; Eingabe : " + zahl)