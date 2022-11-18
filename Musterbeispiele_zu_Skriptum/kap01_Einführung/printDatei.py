print(1, 2, 3)
print(1, 2, 3, sep = '---')
print(1, 2, 3, sep = 'hallo', end = "\nEnde\n")
a = 'abcdefg'
b = 1
c = 12.34
d = (1, 2, 3)
e = [a, b, c]
print(a, b, c, d, e, sep = '-?-', end = "\ndies ist das Ende der print\n")

f = open('datei.txt', 'w')
f = print(1, 2, 3, file = f)
# f.close() bewirkt Fehler??