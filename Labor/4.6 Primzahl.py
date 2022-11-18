def ist_prim(zahl):
    zaehler = 0
    for i in range(1, zahl):
        zahl2 = zahl % i
        if zahl2 == 0:
            zaehler += 1
    if zaehler < 2:
        return True
    if zaehler >= 2:
        return False

x = int(input("Zahl : "))
a = ist_prim(x)
print("Die Zahl ist", a)

prim_list = []
for i in range(2, 50):
    p = ist_prim(i)
    if p == "prim":
        prim_list.append(i)
print(prim_list)