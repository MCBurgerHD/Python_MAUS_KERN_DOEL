from eingabe import inputInt
from random import randint
#                                       min_max
# Wenn der Minimunwert kleiner als der Maximumwert ist, wird dieser umgedreht.
# Zwischen dem Minimunwert und dem Maximumwert werden Zufallszahlen in diesem Bereich erzeugt.
def min_max(mi, ma, anzahl):
    if mi > ma:
        ma1 = mi
        mi = ma
        ma = ma1
    i = 0
    while i <= anzahl:
        zahl = randint(mi, ma)
        i += 1
        print(zahl)

mi = int(input("Minumum : "))
ma = int(input("Maximum : "))
anzahl = int(input("Anzahl : "))

min_max(mi, ma, anzahl)