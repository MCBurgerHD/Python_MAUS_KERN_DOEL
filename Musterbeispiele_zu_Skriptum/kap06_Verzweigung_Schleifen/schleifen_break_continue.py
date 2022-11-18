# break
for i in range(1,6):
    print('Wert von i:', i)
    if i==3:
        break
    print('Wert von 2*i:', 2*i)
print('Schleife beendet')

# continue
for i in range(1,6):
    print('Wert von i:', i)
    if i==3:
        continue
    print('Wert von 2*i:', 2*i)
print('Schleife beendet')
 
# else
for i in range(1,3):
    print('Wert von i:', i)
else:
    print('Else-Zweig')
print('Ende')
