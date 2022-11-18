import cmath            # um komplex zu rechnen

x = 2 + 3j			    # Darstellung einer komplexen Zahl
y = 1 - 4j
z = x * y				# Produkt
print(x + y)			# Summe
print(z)
print(type(z))			# Datentyp
print(z.real, z.imag)	# Bestimmung von Real bzw. Imaginärteil


# Bildung einer Komplexen Zahl über Real- und Imaginärteil
print(complex(2.3, 5.6))
print(cmath.sqrt(-1))
print(cmath.sqrt(x))
print(cmath.phase(x))   # Winkel in Radiant!
print(cmath.phase(1j)*180/cmath.pi)
