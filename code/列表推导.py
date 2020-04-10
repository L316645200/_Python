symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)


import array

array.array('I', (ord(symbol) for symbol in symbols))
array('I', [36, 162, 163, 165, 8364, 164])
