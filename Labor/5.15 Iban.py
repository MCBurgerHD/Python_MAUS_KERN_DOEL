#-----------------------------------------------------
#               ueberpruefung
# Ueberprueft ob der Iban gueltig oder ungueltig ist
#-----------------------------------------------------
def ueberpruefung(iban):
    ibanneu = iban.split(" ")
    ibanneu = str(ibanneu)
    ibanneu = ibanneu[4:19]
    ibanneu = int(ibanneu)
    if ibanneu / 97 % 1:
        return True
    else:
        return False

iban = input("Iban : ")
print(ueberpruefung(iban))