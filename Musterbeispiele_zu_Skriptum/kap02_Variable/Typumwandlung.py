import math

a = 2           # int
b = 2.3         # float
c = a*b         # auch float -> intern umgewandelt
print(c)
s = 'abc'
print(s , 1, sep='')    # funktioniert weil 2 Werte ausgegeben werden
# print(s + 1)    funktioniert nicht weil Typen nicht verträglich
# Typumwandlung (TypeCast) notwendig
print(s + str(1))
a = int("123")
b = float("1.23")
print(a+b)
b = float('1.23e4')
print(b)
# b = float("1.Text")  bewirkt einen Fehler - Umwandlung nicht möglich
