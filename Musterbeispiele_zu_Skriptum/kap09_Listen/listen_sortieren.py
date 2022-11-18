import random
# Texte sortieren
# text = "Hallo Welt"
# text.sort() -> so nicht

# Text als Liste von Zeichen
lst = list('Hallo Welt!')   # Text in Zeichen-Liste verwandelt
lst.sort()      # Liste wird sortiert (alphabetisch nach ASCII-Code)
print(lst)      # [' ', '!', 'H', 'W', 'a', 'e', 'l', 'l', 'l', 'o', 't']

# Texte als Liste von Texten
texte = ["Hallo", "du", "schöne", "weite", "Welt"]
texte.sort()
print(texte)        # ['Hallo', 'Welt', 'du', 'schöne', 'weite']

# Zahlen sortieren
# erzeugt Ganzzahl - Zufallszahlenkette
zahlenList = [random.randint(1, 10) for _ in range(10)] 
print(zahlenList)   # [5, 6, 6, 2, 8, 6, 2, 5, 5, 10]
zahlenList.sort()
print(zahlenList)   # [2, 2, 5, 5, 5, 6, 6, 6, 8, 10]

# erzeugt Dezimalzahl - Zufallszahlenkette
zahlenList = [random.randint(1, 10)/x for x in range(1, 10)] 
print(zahlenList)   
# [4.0, 0.5, 1.3333333333333333, 1.75, 2.0, 0.6666666666666666, 1.4285714285714286, 0.875, 0.7777777777777778]
zahlenList.sort()
print(zahlenList)   
# [0.5, 0.6666666666666666, 0.7777777777777778, 0.875, 1.3333333333333333, 1.4285714285714286, 1.75, 2.0, 4.0]