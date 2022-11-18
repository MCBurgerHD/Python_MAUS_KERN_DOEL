stunde = input('Stundenwert: ')
positiv = stunde.startswith('+') and stunde[1:].isdigit() 
negativ = stunde.startswith('-') and stunde[1:].isdigit()
ganz = stunde.isdigit()
ganzzahl = positiv or negativ or ganz

if not ganzzahl:
    print('Eingabe war keine Zahl')
else:
    zahl = int(stunde)
    if zahl<0:
        print('Stundenwert < 0?')
    elif zahl<12:
        print('Vormittag')
    elif zahl == 12:
        print('Mittag')
    elif zahl<24:
        print('Nachmittag')
    else:
        print('Stundenwert > 24?')
