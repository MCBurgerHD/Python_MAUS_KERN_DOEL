import fractions, decimal

# Brüche
x = fractions.Fraction('1/3')   # Brüche müssen als Texte dargestellt werden
y = fractions.Fraction('2/5')
z = x + y
print(z)
print(x - y)
print(x * y)
print(x / y)

# Dezimalzahlen mit Genauigkeitsangabe
a = decimal.Decimal('0.7')
b = decimal.Decimal('0.9')
c = a + decimal.Decimal('0.1')
d = b - decimal.Decimal('0.1')
print(c == d)
print(c - d)
# c = a - 0.3  mischen von normalen und Decimalen nicht möglich!
print(decimal.Decimal(1)/decimal.Decimal(7))    # 28 Stellen Genauigkeit
decimal.getcontext().prec = 40      # Genauigkeit auf a Stellen umstellen
print(decimal.Decimal(1)/decimal.Decimal(7))

# Bool-Zahlen
a = True
b = 7 == 8
print(b)
print(type(b))
print(~a)
print(not a)
print(~b)
print(not b)
print(3 + a)    # mit logischen Werten rechnen
print(3 - b)
print(int(True))
print(int(False))
print(bool(1))
print(bool(-11.23))
print(bool(0))
print(bool(0.0))
