s = 'abcdefghijklmnopqrstuvwxyz'

print(len(s))               # Liefert die Länge des Strings
sGross = s.upper()          # Verwandelt in Großbuchstabenkette
print(s, sGross)
sKlein = sGross.lower()     # Verwandelt in Kleinbuchstabenkette
print(sGross, sKlein)

print('def' in s)           # enthalten in 
print('df' in s)
print(s.count('def'))       # wieoft ist Text in s enthalten
print(s.count('df'))

print(s.endswith('xyz'))    # Überprüfung auf Text am Ende
print(s.startswith('abc'))  # Überprüfung auf Text am Anfang

text = "Text\tbeinhaltet\teinige\tTabs"
print(text)
print(len(text))
text = text.expandtabs()    # Ersetzt die Tabulatoren durch entsprechende Anzahl von Leerzeichen
print(text)
print(len(text))

print(s.find('efg'))        # Liefert die Startposition für den Suchtext
print(s.find('eg'))         # -1 wenn nicht gefunden
print(text.find('ei', 10))  # beginnt erst ab der angegebenen Indexnummer
print(text.find('ei', 4, 12))   # sucht von a bis b
print(s.rfind('ef'))     # beginnt die Suche von hinten -> höchste Indexnummer

t = ['abc', "Hugo", 'Karl']
print("---".join(t))        # Verknüpft alle Texte miteinander und stellt den Methodenaufrufer jeweils dazwischen

t = s.partition('ef')       # spaltet bei Text auf und liefert ein 3er Tupel
print(t)
t = s.partition('eg')       # spaltet bei Text auf und liefert ein 3er Tupel
print(t)                    # wenn nicht enthalten sind die beiden letzten leer -> keine richtige Aufspaltung
s1 = s.split('ef')          # teilt beim Text auf und liefert eine 2er Liste -> Splittext verschwindet
print(s1)
s1 = s.split('eg')          # teilt nicht - liefert eine 1er Liste - weil nicht enthalten
print(s1)

text = "Dies\nist\nein\nin\nZeilen\ngeteilter\nText"
print(text)
print(text.splitlines())      # spaltet die einzelnen Zeilen auf und liefert eine Liste

text.replace('e', 'a')        # Textobjekt wird nicht verändert - liefert nur neues zurück - dieses wird nicht verwendet
print(text)
text = text.replace('\n', ' ') # Zeilensprüng durch Leerzeichen ersetzen
print(text.replace('e', 'a')) # Ersetzt die Zeichen (für die Ausgabe)
print(text.replace('e', 'a', 3))    # optional mit Maximalanzahl
a = "   Text   "
b = "   noch ein Text   "
print(a, b)
print(a.strip(), b.strip())
