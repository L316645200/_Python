# 用生成器表达式初始化元组和数组
symbols = '$¢£¥€¤'
t = tuple(ord(_) for _ in symbols)
print(t)

import array
a = array.array('h', (ord(symbol) for symbol in symbols))
print(a)

