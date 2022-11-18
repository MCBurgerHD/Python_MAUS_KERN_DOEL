lst = list(range(10, 100, 10))      # erzeugt Liste
print(lst)                          # [10, 20, 30, 40, 50, 60, 70, 80, 90]
lst = list(range(10, 101, 10))      # erzeugt Liste
print(lst)                          # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

zeichenList = list("Hello Python!")
print(zeichenList)      # ['H', 'e', 'l', 'l', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n', '!']

listeNeu = "".join(zeichenList)       # erzeugt Zeichenkette 
print(listeNeu)                       # Hello Python!
listeNeu = "--".join(zeichenList)     # erzeugt Zeichenkette mit '--' als Trenner
print(listeNeu)                       # H--e--l--l--o-- --P--y--t--h--o--n--!
