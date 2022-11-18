#------------------------------------------------------------------------------
# Zählt die Stellen nach dem Buchstaben und schreibt eine Ziffer dahinter
#------------------------------------------------------------------------------
def encode(text):
    wiederholung = 1
    neuertext = ""
    for i in text:
        buchstabe = i
        neuertext += i
        if buchstabe == i:
            wiederholung += 1
        else:
            neuertext += wiederholung
    return neuertext


text = input("Text : ")
print(encode(text))