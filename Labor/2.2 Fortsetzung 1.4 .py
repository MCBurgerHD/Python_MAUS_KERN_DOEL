import math
zuzahlen = float(input("Zu Zahlen : "))
erhalten = float(input("Erhalten : "))

rückgeld = erhalten - zuzahlen
rückgeld = str(rückgeld)

if zuzahlen < erhalten:
    print("Rückgeld :" , rückgeld)

else:
    print("Fehler")