from random import randrange

zahl = randrange(0, 99)
print("Geheimzahl : %d\n" % zahl)

for i in range (1, 7):
    nochmal = True
    while nochmal:
        try:
            n = input("%d.Versuch : " % i)
            n = int(n)
            nochmal = False
        except ValueError:
            print("Fehler - ungültiger Versuch")
    if n == zahl:
        print("richtig!")
        break;
    elif n < zahl:
        print("zu klein")
    else:
        print("zu groß")
#if n!= zahl:
    #print("Anzahl der Maximalversuche erreicht, die Geheimzahl was %d" % zahl)