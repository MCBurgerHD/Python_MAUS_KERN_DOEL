import math
zahl = int(input("Zahl : "))
zahl1 = zahl // 100
zahl2 = zahl // 10
zahl3 = zahl2 % 10
zahl4 = zahl % 10

print(zahl1 , '* 100 +' , zahl3 , ('* 10 +') , zahl4, ('* 1'))