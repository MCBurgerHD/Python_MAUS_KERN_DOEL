# Schreiben einer Liste mit Abständen dazwischen
namen = ["Stefan", "Moritz", "Lutz", "Horst"]
datei = open("beispieldatei3.txt", "w")
for name in namen:
    datei.write(name)
    datei.write(' ')
datei.close()                   # Inhalt: Stefan Moritz Lutz Horst

# Schreiben einer Liste jedes Wort in eine Zeile
datei = open("beispieldatei4.txt", "w")
neueNamen = [text+'\n' for text in namen]
datei.writelines(neueNamen)
datei.close()
