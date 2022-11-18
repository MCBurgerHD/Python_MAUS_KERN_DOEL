#berechnet den Wert von Pi
def reihe(n):
    for i in range(0,n+1):
        if i % 2 == 0:
            n -= 1/(2*i-1)
        else:
            n += 1/(2*i+1)
    return n

n = int(input("n : "))

print(reihe(n))