def filter_duplikate(lst):
    l = list(set(lst))
    return l

lst = list(input("Liste : "))
l = filter_duplikate(lst)
print(l)