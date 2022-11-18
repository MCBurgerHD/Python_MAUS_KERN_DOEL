def betrag(x):      # Bestimmung des Betrags einer Zahl
    if x < 0:
        x = -x
    return x

def wurzel(x):      # Bestimmung der Wurzel
    EPS = 1e-6
    if x >= EPS:
        xAlt = 0
        xNeu = x
        while betrag(xAlt - xNeu) > EPS:
            xAlt = xNeu
            xNeu = 1/2*(xAlt + x/xAlt)
        return xNeu
    else:
        if betrag(x) < EPS:
            return 0.0
        else:
            return -1.0

for i in range(0, 11):      # Berechnung und Ausgabe für die Werte
    x = -1 + i*0.5          # [-1, 4] in Schrittweite 0.5
    result = wurzel(x)
    if result < 0:
        result = "Nicht definiert"
    print(f'x = {x:4.1f}   Wurzel: {result}')
