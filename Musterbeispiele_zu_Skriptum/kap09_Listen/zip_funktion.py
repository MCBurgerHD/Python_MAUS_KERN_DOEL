liste1 = list(range(1, 11))
liste2 = list('abcdefghijklmnopqrstuvwxyz')
liste3 = [x/10 for x in range(1, 8)]

iterator = zip(liste1, liste2)
print(list(iterator))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'i'), (10, 'j')]

iterator = zip(liste2, liste1, liste3)
for i in iterator:
    print(i, end = ' ')
print()
# ('a', 1, 0.1) ('b', 2, 0.2) ('c', 3, 0.3) ('d', 4, 0.4) ('e', 5, 0.5) ('f', 6, 0.6) ('g', 7, 0.7)
