from fractions import Fraction

x = Fraction('1/3')     # der Bruch 1/3 als Fraction-Objekt
print(str(x))           # gut lesbar
print(x)

s = repr(x)
print(s)                # maschinenlesbare Form

y = eval(s)             # Rückumwandlung in ein Objekt
print(y)
