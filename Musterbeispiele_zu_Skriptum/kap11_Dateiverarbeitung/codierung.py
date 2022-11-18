# ohne Konvertierung utf -> nach windows
datei = open("utfText.txt", 'r')
print(datei.read())
datei.close()

# mit Kodierungsangabe - als utf-Text
datei = open('utfText.txt', 'r', encoding='utf8')
text = datei.read()
print(text)
datei.close()

# mit Konvertierung als utf-Text
datei = open("utfText.txt", 'rb')
txt = datei.read()
txt = txt.decode('utf-8')
print(txt)
datei.close()

# aus einer ANSII-Datei
datei = open("ansiiText.txt", 'r')
print(datei.read())
datei.close()
