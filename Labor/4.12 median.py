def berechne_median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 != 0:
        return lst[n//2]
    else:
        arithmetischesmittel = lst[n//2-1] + lst[n//2]
    return arithmetischesmittel

lst = list(input("Liste : "))

median = berechne_median(lst)
print(median)