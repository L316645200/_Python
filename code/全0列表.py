import random

a = [0 for _ in range(3)]
# print(a)
b = [a for _ in range(3)]
for i in range(3):
    for ii in range(3):
        b[i][ii] = i + 1

# print(b)


a = [_ + 3 for _ in range(10)]
print(a)
for i, v in enumerate(a):
    print(v, a[i])

l = [{'time': '2020-03-05T09:26:38Z', 'rate': 1}, {'time': '2020-03-05T09:27:38Z', 'rate': 7},
     {'time': '2020-03-05T09:28:38Z', 'rate': 555}, {'time': '2020-03-05T09:29:38Z', 'rate': 22},
     {'time': '2020-03-05T09:30:38Z', 'rate': 3}, {'time': '2020-03-05T09:31:38Z', 'rate': 0},
     {'time': '2020-03-05T09:32:38Z', 'rate': 6}, {'time': '2020-03-05T09:33:38Z', 'rate': 11},
     {'time': '2020-03-05T09:34:38Z', 'rate': 4}, {'time': '2020-03-05T09:35:38Z', 'rate': 12}]




def fn(x):
    if not x['rate']:
        return 0
    return x['rate']


print(min(l, key=lambda x: x['rate'])['rate'])