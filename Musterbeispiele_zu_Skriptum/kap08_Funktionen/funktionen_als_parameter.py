def gerade(x):
    return x%2 == 0       # gerade - ungerade -> True - False

def ungerade(x):
    return x%2 == 1       # ungerade - gerade -> True - False (nicht exakt)

def loesche(f, liste):
    delList = []  
    for i in liste:
        if f(i):            # wenn Funktion f True
            delList.append(i)
    for i in delList:
        liste.remove(i)   # löscht das entsprechende Element

lst = [1, 2, 3, 4, 4.5, 5, 6, 7, 8, 9, 10]
loesche(gerade, lst)
print(lst)              # [1, 3, 4.5, 5, 7, 9]
loesche(ungerade, lst)
print(lst)              # [4.5]
