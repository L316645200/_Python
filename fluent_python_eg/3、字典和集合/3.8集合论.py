import time
import collections

needles = {'a', 'd'}

haystack = {'a', 'c', 'b'}
found = len(needles & haystack)  # ^ |
print(found)

set1 = frozenset(range(10))
print(set1)

from unicodedata import name

set2 = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(set2)




