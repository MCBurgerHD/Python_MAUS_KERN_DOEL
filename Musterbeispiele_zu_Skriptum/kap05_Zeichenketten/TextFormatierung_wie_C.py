a = 123
print('%d' %a)          # dezimale Ganzzahl
print('%X' %a)          # hexadezimale Ganzzahl
print('%#x' %a)         # hexadezimale Ganzzahl - # bewirkt Kennung 0x vor Zahl
print('%o' %a)          # oktale Ganzzahl
print('%#o' %a)         # oktale Ganzzahl - # bewirkt Kennung 0o vor Zahl
print('%10d' %a)        # Feldbreite - rechtsbündig
print('%1d' %a)         # Mindest-Feldbreite
print('%-10dEnde' %a)   # Feldbreite - linksbündig

b = 123.456
print('%f' %b)          # Flieskommadarstellung - 6 Nachkommastellen
print('%e' %b)          # Exponentialdarstellung - 6 Nachkommastellen
print('%E' %b)
print('%.2f' %b)        # Flieskommadarstellung - 2 Nachkommastellen
print('%.0e' %b)        # Exponentialdarstellung - 0 Nachkommastellen
print('%12.2f' %b)      # Flieskommadarstellung - Feldbreite 12 mit 2 Nachkommastellen

s = 'Text'
print('%s' %s)          # Textdarstellung
print('%10s' %s)        # Textdarstellung mit Feldbreiten rechtsbündig
print('%-10s' %s)       # Textdarstellung mit Feldbreiten linksbündig
print('%10.2s' %s)      # Textdarstellung mit Maximalzeichenanzahl .anz

print('%s ist %d Jahre alt.' %('Matthias', 11))
print('%10s ist %5d Jahre alt.' %('Matthias', 11))
a = 3
print('1/7 mit %d Nachkommastellen: %.3f' %(a, 1/7))
a = 4
s = '%%.%df' %(a)
print(s)
print(('1/7 mit %d Nachkommastellen: ' + s) %(a, 1/7))
print('<img src = "%s" alt="%s" width= "%d">'
         %('foto.jpg', 'Porträt', 200))
