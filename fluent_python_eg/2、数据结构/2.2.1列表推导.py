symbols = '$¢£¥€¤'

codes = [ord(_) for _ in symbols]
print(codes)

codes = [ord(_) for _ in symbols if ord(_) > 127]
print(codes)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

x = 'ABC'
dummy = [ord(x) for x in 'ABC']
print(x)

storage_type = (('10', '容量型本地盘'),
                ('11', '容量型云盘'),
                ('20', '性能型本地盘'),
                ('21', '性能型云盘'),
                ('22', 'LVM云盘'))
# [{'value': 10, 'text': '容量型本地盘'}, {}, {}, {}, {}]


s = [{'value': _[0], 'text': _[-1]} for _ in storage_type]
print(s)