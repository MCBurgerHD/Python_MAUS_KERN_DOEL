# Zuweisungsoperator - links wird ausgewertet und rechts gespeichert
a = 3               
# 3 = a würde Fehler bewirken
print(a)
a = 3 + 4 - 5
print(a)

# Zusammengesetzte Zuweisungsoperatoren -> schreiben immer zurück
a += 3              # erhöhe um -> a = a + 3
print(a)
a -= 3              # vermindere um -> a = a - 3
print(a)
a *= 3              # vervielfache um -> a = a * 3
print(a)
a /= 3              # teile durch -> a = a / 3
print(a)

# Vergleichsoperatoren -> liefern logisches Ergebnis
print(a == 2)       # Vergleich - Inhalt
print(a == 2.0)     # Vergleich 
print(a is 2.0)     # Vergleich - Objekt
print(a is 2)       # Vergleich
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)       # Vergleich - Objekt
print(x is z)       # Vergleich - Objekt

print(a != 3)       # Vergleich - Ungleich 
print(a != 2)       # Vergleich - Nicht gleich
print(x is not y)   # Vergleich - Objekt
print(x is not z)   # Vergleich - Objekt

print(a >= 2)       # Größer gleich
print(a > 2)        # Größer 
print(a <= 2)       # Kleiner gleich
print(a < 2)        # Kleiner

# Enthalten - bei Aufzählungen
print(1 in x)       # ist Wert in der Aufzählung enthalten
print(5 in x)
str1 = "Hallo Welt"
str2 = "Informatik"
print("Hallo" in str1)
print("Hallo" in str2)

a = 'abc'
b = 'abc'
print(a == b)
print(a is b)

a = ['a', 'b', 'c']
b = ['a']
b.append('b')
b.append('c')
print(a, b)
print(a == b)
print(a is b)

a = 4
print(-2 <= a < 5)
print(4 < a < 6)
