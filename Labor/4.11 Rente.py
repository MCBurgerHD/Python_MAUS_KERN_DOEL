def rentenWert(rate, zinssatz, jahre):
    zinswert = zinssatz/100
    i = 1
    kapital = 0
    zwischenergebnis = 0
    while i <= jahre:
        kapital = rate + zwischenergebnis
        zwischenergebnis = kapital * zinswert
        print(kapital)
        i += 1
    return kapital


rate = float(input("höhe der Rate : "))
zinssatz = float(input("Zinswert : "))
jahre = int(input("Jahresanzahl : "))
kapital = rentenWert(rate, zinssatz, jahre)

print(kapital)