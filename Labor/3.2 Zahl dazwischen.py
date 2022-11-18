a = int(input("1. Zahl :"))
b = int(input("2. Zahl :"))

if a == b:
    print("Fehler")
elif a < b:
    i = a
    for i in range(a, b):
        print(i)
elif a > b:
    i = b
    for i in range(a, b, -1):
        print(i)

print("")

if a == b:
    print("Fehler")
elif a < b:
    while i < b:
        print(i)
        i -= 1
    print("Ende")
elif a > b:
    while i < a:
        print(i)
        i += 1
    print("Ende")
