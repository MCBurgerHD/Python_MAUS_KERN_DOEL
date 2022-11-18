lst = list(range(10, 101, 10))
print(lst)          # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

lstNeu = [x*2 + 1 for x in lst]
print(lstNeu)       # [21, 41, 61, 81, 101, 121, 141, 161, 181, 201]

lstNeu = [[x, x**2]  for x in lst]
print(lstNeu)       # erzeugt eine geschachtelte (2-dim.) Liste
# [[10, 100], [20, 400], [30, 900], [40, 1600], [50, 2500], [60, 3600], [70, 4900], [80, 6400], [90, 8100], [100, 10000]]

for x in lst:
    print(x, x*x, x**3, sep = '\t')
    