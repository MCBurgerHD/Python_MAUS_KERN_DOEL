import re

x = input('Text: ')

if x.isdigit():
    print('{} besteht nur aus Ziffern'.format(x))
    print('Kann Text mit int() in eine positive Ganzzahl verwandeln')
    y = int(x)
    print(x, 2*y)
else:
    print('{} besteht nicht nur aus Ziffern'.format(x))

print('Jetzt geht es weiter')

pattern = r'^[\+-]?\d+\.?\d*$'
if re.match(pattern, x):
    print("Entspricht einem float")
    y = float(x)
    print(x, 2*y)
else:
    print('Entspricht nicht einem float')
