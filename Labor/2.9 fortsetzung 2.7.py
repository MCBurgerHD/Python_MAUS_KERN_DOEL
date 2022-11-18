import math
monat = int(input("Monat :"))
jahr = int(input("Jahr :"))

if monat == [1 , 3 , 5 , 7 , 8 , 10 , 12]:
    print("Das Monat hat 31 Tage")
elif monat == [2 , 4 , 6 , 9 , 11]:
    print("Das Monat hat 30 Tage")
elif math.fmod(jahr,4)==0:
    print("Das Monat hat 29 Tage")
else:
    print("Das Monat hat 28 Tage")