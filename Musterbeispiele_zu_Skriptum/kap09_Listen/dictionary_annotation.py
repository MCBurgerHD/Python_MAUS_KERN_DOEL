from typing import List, Set, Dict, Tuple

lst: List[int]      # Vorschlag - Liste von Integer
lst = [1, 2, 3, 4]
print(lst)          # [1, 2, 3, 4]
lst = [(1,'a'), (2,'b')]    # leider möglich -> Liste von Tupeln
print(lst)          # [(1, 'a'), (2, 'b')]

set: Set[str] = {'a', 'ab', 'abc'}
print(set)          # {'a', 'abc', 'ab'}
tuple: Tuple[int, str]
tuple = (1,'a')
print(tuple)        # (1, 'a')
dic: Dict[str, float] = {'abc': 1.1, 'bcd': 2, 'ab': 3.14}
print(dic)          # {'abc': 1.1, 'bcd': 2, 'ab': 3.14}
