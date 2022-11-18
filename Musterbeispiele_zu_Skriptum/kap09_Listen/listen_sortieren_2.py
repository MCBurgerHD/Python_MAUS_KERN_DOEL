import random

lst = list("Hallo Welt!")
listNeu = sorted(lst)       # lst bleibt unverändert - neue List erzeugt
print(lst)                  # ['H', 'a', 'l', 'l', 'o', ' ', 'W', 'e', 'l', 't', '!']
print(listNeu)              # [' ', '!', 'H', 'W', 'a', 'e', 'l', 'l', 'l', 'o', 't']

zahlenList = [random.randint(1, 9) for x in range(1, 10)] 
print(zahlenList)           # [3, 7, 8, 2, 2, 1, 6, 4, 5]
print(sorted(zahlenList))   # [1, 2, 2, 3, 4, 5, 6, 7, 8]
print(zahlenList)           # [3, 7, 8, 2, 2, 1, 6, 4, 5]
