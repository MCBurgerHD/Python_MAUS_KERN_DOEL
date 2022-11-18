# logische (boolsche) Operatoren
a = True
b = False
print(a and a)          # logisches und r + r -> r
print(a and b)          # logisches und r + f -> f
print(b and a)          # logisches und f + f -> f
print(b and b)          # logisches und f + r -> f
print(a or a)           # logisches oder  r o r -> r
print(a or b)           # logisches oder  r o f -> r
print(b or a)           # logisches oder  f o r -> r
print(b or b)           # logisches oder  f o f -> f
print(not a)            # logische Verneinung nicht richtig = falsch
print(not b)            # logische Verneinung nicht falsch = richtig

# Bitoperatoren - verändern das Bitmuster und daduch den Zahlenwert!
a = 15                  # Bitmuster  1111
print("a =", a)
print('a = {0: b}'.format(a))
print(a << 1)           # Bitmuster  11110 - um eins nach links geschoben - a*2
print('a = {0: b}'.format(a<<1))
print(a << 2)           # Bitmuster  111100 - um 2 nach links geschoben - a*2^2
print('a = {0: b}'.format(a<<2))
print(a << 4)           # Bitmuster  11110000 - um 4 nach links geschoben - a*2^4
print('a = {0: b}\n'.format(a<<4))

a = 288                 # Bitmuster  100100000
print("a =", a)
print('a = {0: b}'.format(a))
print("a =", a>>1)      # Bitmuster  10010000- um eins nach rects geschoben - a/2
print('a = {0: b}'.format(a>>1))
print("a =", a>>5)      # Bitmuster  10010000- um 5 nach rects geschoben - a/(2^5)
print('a = {0: b}'.format(a>>5))
print("a =", a>>6)      # Bitmuster  10010000- um 6 nach rects geschoben - a/(2^6)
print('a = {0: b}'.format(a>>6))        # Ganzzahldivision

# binäre Verknüpfungen
a = 288                 # Bitmuster  100100000
b = 200                 # Bitmuster  011001000
print('a = {0: 10b}'.format(a))
print('b = {0: 10b}'.format(b))
print('c = {0: 10b}'.format(a&b))   # bitweises und
print('c = {0: 10b}'.format(a|b))   # bitweises oder
print('c = {0: 10b}'.format(a^b))   # bitweises ausschließendes oder
print('c = {0: 10b}'.format(~a))    # bitweise Verneinung - Kippen
print('c = {0: 10b}'.format(~b))
print('c = {0: 10b}'.format(199))
print('c = {0: 10b}'.format(~199))
