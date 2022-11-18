datei = open('textdatei.txt', 'r')
text = datei.read(20)   # liest nur maximal 20 Zeichen
print(text)             # Dies ist Zeile 1
                        # Die
text = datei.read(20)   # s ist Zeile 2
print(text)             # Dies i
text = datei.read()     # liest den gesamten Rest
print(text)             # st eine weitere Zeile 3
                        # Einmal noch 4
                        # Dies ist die letzte Text-Zeile 5 - danach noch Leerzeile!

datei.seek(0, 0)        # stellt den Schreiblese-Marker an den Dateianfang
zeile = datei.readline()    # liest nur eine Zeile
print(zeile)                # Dies ist Zeile 1 - mit '\n' - also Zeilensprung am Ende!
zeile = datei.readline()    # 
print(zeile)                # Dies ist Zeile 2 - mit '\n'

datei.seek(0)               # entspricht seek(0, 0)
liste = datei.readlines()   # liefert Liste aller Zeilen
print(liste)
# ['Dies ist Zeile 1\n', 'Dies ist Zeile 2\n', 'Dies ist eine weitere Zeile 3\n', 
#  'Einmal noch 4\n', 'Dies ist die letzte Text-Zeile 5\n']

datei.seek(0)
liste = datei.readlines(50)   
# liefert Liste - liest mind. 50 Byte + Rest der angefangenen Zeile
print(liste)    # Liste ganzer Zeilen!
# ['Dies ist Zeile 1\n', 'Dies ist Zeile 2\n', 'Dies ist eine weitere Zeile 3\n']
liste = datei.readlines(50)  
print(liste)
# ['Einmal noch 4\n', 'Dies ist die letzte Text-Zeile 5\n']

datei.seek(0)
for line in datei:
    print(line, end='') # Aufgrund des Zeilensprungs im Text end = ''


datei.close()       # Datei schliessen
