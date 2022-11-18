
#           filter_duplikate
# filtert Duplikate aus der Liste herraus
def filter_duplikate(lst):
    lst1 = []
    for i in lst:
        if lst1.count(i) == 0:
            lst1.append(i)
    return lst1

#               konvertiere_in_zahlen
#Verwandelt alle gleichen Buchstaben/Worte in die gleiche Zahl
def konvertiere_in_zahl(lst):
    lst1=filter_duplikate(lst)
    lst2 = []
    for i in lst:
        index = lst1.index(i)
        lst2.append(index)
    return lst2
lsta = ["G", "A", "J", "A", "J", "G"]
lstb = ["GER", "USA", "AUT", "GER", "AUT"]
lstc = ["A", "B", "C", "0", "1", "42"]

lsa = konvertiere_in_zahl(lsta)
lsb = konvertiere_in_zahl(lstb)
lsc = konvertiere_in_zahl(lstc)