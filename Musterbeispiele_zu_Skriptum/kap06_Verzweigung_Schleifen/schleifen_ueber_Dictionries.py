dict = {'a':12, 'e':45, 'c': 13, 'b':23}
resultList = [x for x in dict]
resultSet = {x for x in dict}
print(resultList)           # ['a', 'e', 'c', 'b']
print(resultSet)            # {'a', 'e', 'b', 'c'}

resultList = [k for k,v in dict.items()]
resultSet = {v for k,v in dict.items()}
resultDic = {k: v*2 for k,v in dict.items()}
print(resultList)           # ['a', 'e', 'c', 'b']
print(resultSet)            # {13, 12, 45, 23}
print(resultDic)            # {'a': 24, 'e': 90, 'c': 26, 'b': 46}
