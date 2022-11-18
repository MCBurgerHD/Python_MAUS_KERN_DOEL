print('{} ist {} Jahre alt'.format('Sebastian', 13))    # beliebige Werte
print('{1} ist {0} Jahre alt'.format(13, 'Sebastian'))  # nummerierte Parameter
print('{name} ist {alter} Jahre alt'.format(alter=13, name='Sebastian'))  # benannte Parameter

# Ganzzahldarstellung
print('Zahl1: {:d} und Zahl2: {:d}'.format(12,23))     
print('Zahl1: {:>7d} und Zahl2: {:<7d} Ende'.format(12,23))  # rechts- bzw. linksbündig
print('Zahl1: {:7d} und Zahl2: {:^7d} Ende'.format(12,23))   # rechtsbündig bzw. zentriert

# Dezimalzahldarstellung
print('Zahl1: {:f} und Zahl2: {:e}'.format(12.23,123.45))   # Standard 6 Nachkommastellen
print('Zahl1: {:.1f} und Zahl2: {:.3E}'.format(12.23,123.45))   # setzen der Nachkommastellen
print('Zahl1: {:7.1f} und Zahl2: {:<10.3E} Ende'.format(12.23,123.45))   # mit Feldbreiten
print('Zahl1: {:,f} '.format(12123.45))   # Tausendertrennzeichen
print('Zahl1: {:n} '.format(12123.45))    # Lokalisierung
print('Zahl1: {:n} '.format(12.12345))    # Lokalisierung
print('Zahl1: {:n} '.format(1234512.12345))    # Lokalisierung

# Textdarstellung
print('Text: {:s}'.format('Hallo Welt'))
print('Text: {:>20s}'.format('Hallo Welt'))     # Feldbreite
print('Text: {:>20.5s}'.format('Hallo Welt'))   # maximale Zeichenanzahl
