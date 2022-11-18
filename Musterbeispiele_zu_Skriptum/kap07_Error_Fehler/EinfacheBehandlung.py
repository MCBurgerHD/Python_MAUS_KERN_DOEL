try:
    zahl = input('Zahl eingeben: ')
    zahl = int(zahl)
    print(zahl, 3*zahl)
except Exception:
    print('Exception gefangen')
    exit()
print('Ende')
