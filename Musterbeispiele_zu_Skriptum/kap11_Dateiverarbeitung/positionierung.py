datei = open('textdatei.txt', 'r')  # als Textdatei
print(datei.tell())         # 0 Byte entfernt - Dateianfang
datei.read(15)
print(datei.tell())         # 15 Byte entfernt
datei.read(15)
print(datei.tell())         # 31 Byte entfernt wegen Zeilensprungkonvertierung = 2 Byte \r\n
datei.seek(100, 0)
print(datei.tell())         # 100 Byte entfernt
try:
    datei.seek(-12, 2)      # Modus t -> nur vom Dateianfang
except:
    print('Bei Textmodus nicht möglich!')
datei.seek(300)             # Position hinter dem Dateiende
print(datei.tell())         # 300 Byte entfernt - ändert keine Größe!
print(datei.read())         # liefert Leerstring - hinter dem Dateiende
datei.close()

datei = open('textdatei.txt', 'rb')  # als Binärdatei
datei.read(15)
print(datei.tell())         # 15 Byte entfernt
datei.read(15)
print(datei.tell())         # 30 Byte entfernt Zeilensprung bleibt als 2 EinzelByte
datei.seek(-16, 2)          # -16 Byte vor dem Ende
print(datei.tell())         # 100 Byte entfernt
datei.seek(-16, 1)          # -16 Byte vor der aktuellen Position
print(datei.tell())         # 84 Byte entfernt
datei.read()
print(datei.tell())         # 116 Byte entfernt - Dateiende
leertext = datei.read()     # Lesen am Ende
print(leertext)             # liefert Leerzeile als b''
