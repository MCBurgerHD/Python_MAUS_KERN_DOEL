def merge_lists(lst1, lst2):
    lst1.extend(lst2)
    lst1 = list(set(lst1))
    return lst1

lst1 = [1, 2, 1]
lst2 = [1, 3, 2] 

l = merge_lists(lst1, lst2)

print(l)