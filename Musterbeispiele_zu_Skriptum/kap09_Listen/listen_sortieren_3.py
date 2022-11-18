lst = list("Hallo Welt!")
mysort = sorted(lst, key= str.lower)
print(mysort)       # [' ', '!', 'a', 'e', 'H', 'l', 'l', 'l', 'o', 't', 'W']
mysort = sorted(lst, reverse=True)
print(mysort)       # ['t', 'o', 'l', 'l', 'l', 'e', 'a', 'W', 'H', '!', ' ']
mysort = sorted(lst, key= str.lower, reverse=True)
print(mysort)       # ['W', 't', 'o', 'l', 'l', 'l', 'H', 'e', 'a', '!', ' ']
