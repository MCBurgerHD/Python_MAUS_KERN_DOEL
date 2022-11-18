datei = open('textDateiMitPrint.txt', 'w')
print('Zeile 1', file=datei)    # Zeile mit Zeilensprung
print('', file=datei)           # Leerzeile
print('Zeile 3', file=datei, end='')    # Zeile ohne Zeilensprung
print('Zeile 4')                # Schreibt auf die normale Konsole
print('\nZeile4\nZeile5', file=datei)   # 3 weitere Zeilen hinzugefügt
