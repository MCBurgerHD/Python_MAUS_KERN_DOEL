d = {k:chr(65) for k in range(5)}
print(d)        # {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
print(len(d))   # Länge 5

for i in d.keys():
    print(i, ':', d[i])