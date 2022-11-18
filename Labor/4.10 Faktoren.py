def faktorisiere(n):
    if n <= 0:
        return 0,0
   
    p = 1
    q = n
    t = p
    while t + 1 < q:
        if n %t == 0:
            p = t
            q = n // p
        t += 1
    return p, q

zahl = int(input("Zahl : "))
zahl2 = faktorisiere(zahl)
print("p : " , zahl2[0], "q : " , zahl2[1])