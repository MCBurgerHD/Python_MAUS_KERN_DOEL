#                        listsum
# erechent dur zwei ineinander geschachtelte Schleifen die Summe-
# der Zahlen in der Liste.
def listsum(lst):
    text = 0
    for i in lst:
        for m in i:
            text = text + m
    return text

lst = [[1],[2],[3]]
listensumme = listsum(lst)
print(listensumme)