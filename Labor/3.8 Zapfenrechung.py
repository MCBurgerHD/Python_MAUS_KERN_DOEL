zahl = int(input("positive Ganzzahl : "))

zahl1 = zahl

i = 1
while i < 9:
    i += 1
    zahl = zahl * i
    print( zahl , "*" , i )
while i > 1:
    zahl = zahl / i
    print( zahl , "/" , i )
    i -= 1