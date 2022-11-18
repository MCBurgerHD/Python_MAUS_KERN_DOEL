import math

print(" Programm zur Berechnung von Umfang, "
"Fläche und Diagonalen eines Quadrates")
a = input("Seitenlänge a = ")

# A = a * a Fehler : a ist ein String , wir wollen aber
#mit Zahlen rechnen
a = float(a)
A = a * a
A = a ** 2     #** => hoch
print("Fläche =", A)

d = math.sqrt(2 * a ** 2)     #2a^2
print("Diagonale =", d)