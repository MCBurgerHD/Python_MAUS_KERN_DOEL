#-----------------------------------------------------------------
#                     klammerpruefung
# Ueberprueft ob die geoeffnete Klammer auch geschlossen wurde
#-----------------------------------------------------------------
def klammerpruefung(text):
    klammernauf = ("(", "[", "{")
    kalmmerzu = (")", "]", "}")
    for i in text:
        if i in klammernauf or i in kalmmerzu:
            return "korrekt"
        else:
            return "falsch"

klammertext = input("Kalmmern : ")
print(klammerpruefung(klammertext))