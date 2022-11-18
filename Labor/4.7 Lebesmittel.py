def bestimme_naehrwet(fett, kohlenhydrate, eiweis):
    aufschlussfett = 9.3
    aufschlusskohlenhydrate = 4.1
    aufschlusseiweis = 4.1
    kcalfett = aufschlussfett * fett
    kcalkohlenhydarte = aufschlusskohlenhydrate * kohlenhydrate
    kcaleiweis = aufschlusseiweis * eiweis
    kcal = kcaleiweis + kcalfett + kcalkohlenhydarte
    return kcal

fett = float(input("Fette : "))
kohlenhydrate = float(input("Kohlehydrate : "))
eiweis = float(input("Eiweiß : "))

kcal = bestimme_naehrwet(fett, kohlenhydrate, eiweis)
print("{:.2f}".format(kcal), "kcal")
