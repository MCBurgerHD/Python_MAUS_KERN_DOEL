import math

#ueberprueft ob zwei laengen kleiner als die dritte ist
def isDreieck(a, b, c):
    if a + b < c:
        dreieck = False
    elif c + b < a:
        dreieck = False
    elif a + c < b:
        dreieck = False
    elif a + b > c:
        dreieck = True
    elif a + c > b:
        dreieck = True
    elif c + b > a:
        dreieck = True
    return dreieck

#berechnet die Flaeche des Dreiecks, wenn die Funktion isDreieck True liefert
def flaeche(a, b, c):
    if isDreieck(a, b, c) == False:
        return 0.0
    if isDreieck(a, b, c) == True:
        s = (a+b+c)/2
        A = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return A

a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

flaecheninhalt = flaeche(a, b ,c)

print("Fläche : " , flaecheninhalt)