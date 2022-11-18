def grundumsatz(geschlecht, masse, groesse, alter):
    if geschlecht == "m":
        kcal = 66.5 + 13.7 * masse + 5 * groesse - 6.8 * alter
    elif geschlecht == "w":
        kcal = 665 + 9.6 * masse + 1.8 * groesse - 4.7 * alter
    return kcal

geschlecht = input("m/w : ")
masse = float(input("Masse : "))
groesse = int(input("Größe : "))
alter = int(input("Alter : "))

i = 50
while i <= 80:
    print(i)
    j = 160
    while j <= 180:
        print(j)
        j += 5
        kcal = grundumsatz(geschlecht, i, j, alter)
        for z in range(50, 50, 5):
            print(z, end=" ")
            for s in range(160, 180, 5):
                print(z, s, end=" ")
            print(round(kcal))
    i += 5