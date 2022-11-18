zahl = input('Geben Sie eine Zahl ein: ')

if not str.isdigit(zahl):
    raise TypeError("Keine Zahl")
else:
    print('Eingabe war eine Zahl')

print('Wir machen weiter')
