def harmonischeReihe(n):
    sum=0.0
    for i in range(n):
        sum = sum + 1.0/(i+1)
    return sum    

wert = 1
while wert <= 100000000:
    erg = harmonischeReihe(wert)
    print("{:11d] | {10.6f]}".format(wert, erg))
    wert *= 10