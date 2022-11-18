(a, b, c) = (1, 2, 3)
print((a, b, c))    # (1, 2, 3)
print(a, b, c)      # 1 2 3

a, b, c = 11, 12, 13
print((a, b, c))    # (11, 12, 13)
print(a, b, c)      # 11 12 13

print((a, b, c) == (11, 12, 13))    # True
print((a, b, c) == (11, 11, 13))    # False
print((a, b, c) != (11, 11, 13))    # True
# Achtung - kein Weglassen der KLammern
print(a, b, c == 11, 12, 13)        # 11, 12, False, 12, 13

print((1, 2, 3) < (1, 2, 3))        # False
print((1, 2, 3) < (2, 2, 3))        # True
print((1, 2, 4) < (1, 2, 3))        # False
print((1, 2) < (1, 2, 3))           # True
print((1, 2, 3, 4) < (1, 2, 3))     # False

a = 12; b = 23; c = 45
(a, b) = (b, a)
print(a, b, c)         # 23 12 45
# oft werden die Klammern weggelassen
a, b, c = b, c, a
print(a, b, c)         # 12 45 23
