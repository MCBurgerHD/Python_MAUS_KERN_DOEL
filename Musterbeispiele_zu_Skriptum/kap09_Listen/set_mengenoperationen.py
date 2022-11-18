set1 = {1, 3, 5, 7, 9, 11}
set2 = {1, 2, 3, 4, 5, 6, 7}

# Vereinigung
print(set1 | set2)   # {1, 2, 3, 4, 5, 6, 7, 9, 11}
# Durchschnitt
print(set1 & set2)   # {1, 3, 5, 7}
# Differenz
print(set1 - set2)   # {9, 11}
# Unterschied
print(set1 ^ set2)   # {2, 4, 6, 9, 11}
print(set1)          # {1, 3, 5, 7, 9, 11}
print(set2)          # {1, 2, 3, 4, 5, 6, 7}
