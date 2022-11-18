import math

jahr=int(input("Jahr:"))
 
if math.fmod(jahr,400)==0:
    print(jahr, "Schaltjahr")
elif math.fmod(jahr,100)==0:
    print(jahr, "Schaltjahr")
elif math.fmod(jahr,4)==0:
    print(jahr, "Schaltjahr")
else:
    print(jahr, "kein Schaltjahr")