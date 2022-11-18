# Datei "beispieldatei1.txt" für den Schreibvorgang öffnen
datei = open("beispieldatei.txt", "w")
# Den Text "Hallo Welt!" in die Datei schreiben
datei.write("Hallo Welt")
# speichern und schliessen      # Inhalt: Hallo Welt
datei.close()

# Schreiben einer Liste
namen = ["Stefan", "Moritz", "Lutz", "Horst"]
datei = open("beispieldatei2.txt", "w")
for name in namen:
    datei.write(name)
datei.close()                   # Inhalt: StefanMoritzLutzHorst

namen = ["Stefan", "Moritz", "Lutz", "Horst"]
datei = open("beispieldatei2.txt", "w")
datei.writelines(namen)
datei.close()
