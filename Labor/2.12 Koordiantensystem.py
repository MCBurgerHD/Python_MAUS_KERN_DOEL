x = int(input("x :"))
y = int(input("y :"))

if x == 0 and y == 0:
    print("Die Koordiante ist im Ursurung")
elif x == 0:
    print("Die Koordinate x ist auf der x-Achse")
elif y == 0:
    print("Die Koordinate y ist auf der y-Achse")
elif x < 0 and y > 0:
    print("Die Koordinate liegt auf dem 2.Quadranten")
elif x > 0 and y > 0:
    print("Die Koordinate liegt auf dem 1.Quadranten")
elif y < 0 and x > 0:
    print("Die Koordinate liegt auf dem 4.Quadranten")
elif y < 0 and x < 0:
    print("Die Koordinate ist im 3.Quadranetn")
