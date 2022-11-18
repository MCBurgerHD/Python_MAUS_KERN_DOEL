lst = [1, 2, 3, 'abc', 'efg', 15.4]

print(lst[2])               # das 3.Element -> 3
print(lst[3])               # das 3.Element -> abc
print(lst[2:4])             # das 3.und 4.Element -> [3, 'abc']
print(lst[ : : -1])         # umgekehrt Reihenfolge  [15.4, 'efg', 'abc', 3, 2, 1]
lst[1] = 1                  # ändert den Wert
print(lst)                  # [1, 1, 3, 'abc', 'efg', 15.4]

# mehrdimensionale Liste
mlst = [[1,2], ['abc', 'efg']]
print(mlst[0])              # [1, 2]
print(mlst[0][1])           # 2
