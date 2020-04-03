from functools import reduce

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
    print(i, end=', ')

print(a)
for i in a:
    print(i, end=', ')

n = 10
a = [i * i for i in range(n)]
print(a)

l = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]


def counter(c, n):
    print('c=%d' % c, 'n=%d' % n)
    if n == 1:
        c += 1
    return c


l = l[0] + l[1] + l[2] + l[3]
print(l)
print(reduce(counter, l))
