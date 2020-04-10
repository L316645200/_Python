import os

d = divmod(20, 8)  # 获取商 和 余数
print(d)

_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(_, filename)

i = 2
print(1 < i < 3)  # False
print(1 < i <= 3)  # True

import sys

print(sys.argv[0])

print(os.getcwd())

l = [1, 2, 3, 4]
print(l[0:1])

for i in [1, 2, 3, 4]:
    print(i)
    if i > 2:
        print(i)
        break
else:
    print(i, '我是else')


def get_square(n):
    for i in range(n):
        yield (pow(i, 2))


a = get_square(5)
for i in a:
    print('pow=%d' % i, end=', ')

print(a)
for i in a:
    print(i, end=', ')

n = 10
a = [i * i for i in range(n)]
print(a)

print(2 ** 31 - 1)

l = [1, 2, 3, 4, 5]
l2 = l.copy()
print(l2)
