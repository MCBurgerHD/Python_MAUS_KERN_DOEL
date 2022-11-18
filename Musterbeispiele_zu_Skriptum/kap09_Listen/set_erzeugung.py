from random import randint

s = {2, 3, 4, 1, 3, 1, 5, 4}
print(s)                # {1, 2, 3, 4, 5}  - Duplikate werden entfernt

s = set("Hallo neue Welt!")
print(s)                # {'o', 'n', ' ', 'e', '!', 't', 'W', 'u', 'H', 'a', 'l'}

l = [randint(1, 9) for _ in range(10)]
print(l)                # [4, 8, 8, 4, 8, 9, 4, 9, 3, 6]
s = set(l)
print(s)                # {3, 4, 6, 8, 9}
