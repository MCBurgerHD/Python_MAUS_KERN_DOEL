from array import array

def printList(l):
    for i in l:
        print(i, end = ' ')
    print()

a = array('i', [1, 7, 12, -5, 36])
print(a)            # array('i', [1, 7, 12, -5, 36])
printList(a)        # 1 7 12 -5 36
print(a[2])         # 12
print(a[1:3])       # array('i', [7, 12]) -> View auf Teilarray
printList(a[1:3])   # 7 12
a.append(25)
printList(a)        # 1 7 12 -5 36 25
print(len(a))       # 6
try:
    a.append(3.14)  # kann nicht hinzugefügt werden
except TypeError:
    print("Falscher Datentyp")
printList(a)    # unverändert

# a = array('h', [1, 7, 12, -5, 40000])    40000 zu groß -> OverflowError
a = array('i', [1, 7, 12, -5, 40000])
printList(a)        # 1 7 12 -5 40000

# a = array('i', [1, 7, 12, -5, 400.00])    TypeError wegen double
a = array('f', [1, 7, 12, -5, 400.00])
printList(a)        # 1.0 7.0 12.0 -5.0 400.0

a.append(2000000000)
# a.append(4000000000)  4000000000 zu groß -> OverflowError
printList(a)        # 1 7 12 -5 40000 2000000000


a = array('u', 'hello')
printList(a)        # h e l l o
a.append('W')
printList(a)        # h e l l o W
# a.append('orld')  -> nicht möglich - nur Einzelzeichen - unicode character
for c in 'orld':    # so möglich
    a.append(c)
printList(a)        # h e l l o W o r l d
print(a[5])         # W
print(a[3:6])       # array('u', 'loW')
print(''.join(a[3:6]))  # verbindet die Einzelzeichen zu einer Kette -> String

a.remove('o')       # löscht erstes o
printList(a)        # h e l l W o r l d
a.remove(a[1])      # löscht e
printList(a)        # h l l W o r l d

a.insert(0, 'A')    # A vorstellen
printList(a)        # A h l l W o r l d
a.insert(-2, 'Z')   # Z als vorvorLetztes
printList(a)        # A h l l W o r l d
