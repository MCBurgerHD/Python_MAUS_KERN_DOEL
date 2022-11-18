try:
    datei = open('schreibeLeseDatei.txt', 'r+')
    datei.close()
except:
    print('Datei muss existieren')

datei = open('schreibeLeseDatei.txt', 'w+', encoding='utf-8')
datei.write('Name: First Line\n')
datei.write('Person: Second Line\n')
datei.write('Student: Third Line\n')    # 3 Textzeilen
datei.seek(0)                           # rücksetzen
print(datei.read())                     # lesen und ausgeben
datei.write('4te-Zeile')                # noch eine Zeile
datei.seek(0)                           # rücksetzen
datei.write('First Line\n')             # Achtung
datei.write('Second Line\n')            # Zeilen sind kürzer
datei.write('Third Line\n')             # es wird nicht alles überschrieben!

'''
datei.seek(0)
datei.write('Dies ist dafür aber eine ganz lange Zeile, \
welche den gesamten Text welcher aus mehreren Zeilen bestand, \
überschreibt')
'''

datei.close()
