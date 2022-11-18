def inputInt(text):
    nochmal = True
    while nochmal:
        zahl = input(text)
        try:
            zahl = int(zahl)
            nochmal = False
        except Exception:
            print("Eingabe ist nicht korrekt - Wiederholung!")
    return zahl