"""
fobj = open("uebungsdateien/blindtext.txt", "r")
for line in fobj:
    print(line.rstrip())    # print(line, end="")
fobj.close()

f = open("blindtext.txt", "r")
print(f.readline()) # 1. Zeile
print(f.readline()) # 2. Zeile
print(f.readline(5)) # 5. Zeichen der 3. Zeile

fobj = open("blindtext.txt")
zeile = fobj.readline()
while zeile!="":
    print(zeile, end="")
zeile = fobj.readline()

f = open("blindtext.txt")
lst = f.readlines() # Gesamter Inhalte in Liste lst gelesen
print(lst[3]) # z.B. 3. Element (= 3. Zeile) ausgeben

f = open("blindtext.txt")
lst = [line.rstrip() for line in f.readlines()]

f = open("blindtext.txt").readlines()
print(f[3])

blindstr = open("blindtext.txt").read()
print(blindstr)

file = open("test.txt","w") # Datei zum Schreiben öffnen/erstellen
file.write("Test1\n") # Zeile1 mit “Test1” und Umbruch schreiben
file.write("\n") # Zeile2 nur Umbruch schreiben
file.write("Test2\n") # Zeile 3 mit “Test2” und Umbruch schreiben
file.close() # Datei schließen

fobj_in = open("blindtext.txt")
fobj_out = open("blindtext_nr.txt","w")
i = 1
for line in fobj_in:
    print(line.rstrip())
    fobj_out.write(str(i) + ": " + line)
    i = i + 1
fobj_in.close()
fobj_out.close()

f = open("demofile.txt", "w")
f.write("Woops! Jetzt ist alles weg!")
f.close()

f = open("demofile.txt", "a")
f.write("\nJetzt hat die Datei mehr Inhalt!\n")
f.close()

with open("blindtext.txt") as fobj:
    for line in fobj:
        print(line.rstrip())

with open("blindtext.txt") as fobj_in:
    with open("blindtext_nr.txt","w") as fobj_out:
        i = 1
for line in fobj_in:
    print(line.rstrip())
fobj_out.write(str(i) + ": " + line)
i = i + 1

with open("blindtext.txt") as fobj_in, \
open("blindtext_nr.txt","w") as fobj_out:
    i = 1
for line in fobj_in:
    print(line.rstrip())
fobj_out.write(str(i) + ": " + line)
i = i + 1

try:
# in eine Textdatei schreiben
    with open('testfile.txt', 'w') as f1:
    f1.write('Hier wird ein Text geschrieben!\n')
    f1.write('Unicodes äöüß\n')
# Textdatei zeilenweise auslesen
    with open('testfile.txt', 'r') as f2:
    for line in f2:
        print(line, end='')
    except BaseException as err:
        print('Fehler:', err)
    
with open("uebungsdatei/eigeneDatei.txt","r",encoding="utf-8") as f:
    print(f.read())
"""