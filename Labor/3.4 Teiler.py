zahl = int(input("Zahl :"))

i = zahl

if zahl == 0 or zahl < 0:
    print("Fehler")
while i > 0:
    if i % 2 == 0:
        print("{:d}".format(i))
    i -= 2