keyList = list(range(1, 11))
valueList = list(chr(x) for x in range(97, 107))
print(keyList)      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(valueList)    # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
iterable = zip(keyList, valueList)  # Bildung der Schlüssel-Werte-Paare
d = dict(iterable)  # Verwandlung in Dictionary
print(d)    # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j'}
