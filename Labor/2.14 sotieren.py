a = int(input("1. Zahl :"))
b = int(input("2. Zahl :"))
c = int(input("3. Zahl :"))

if c < b:
    d = c
    c = b
    b = d
elif c < a:
    d = c
    c = a
    a = d
elif b < a:
    d = b
    b = a
    a = d
print(a , "," , b , "," , c)