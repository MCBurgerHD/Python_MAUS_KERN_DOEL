nochmal = True
while nochmal:
    text = input("Ganzzhal : ")
    ganz = text.isdigit()
    negativGanz = text[0]=="-" and text[1:].isdigit()
    positivGanz = text[0]=="+" and text[1:].isdigit()
    if not ganz and not negativGanz and not positivGanz:
        print('Fehlerhafte Eingabe - Wiederholung\n')
    else:
        nochmal = False
print('Eingabe ist die Ganzzahl:', int(text))