from functools import reduce


def counter(c, n):
    print('c=%d' % c, 'n=%d' % n)
    if n == 1:
        c += 1
    return c


l = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

l = l[0] + l[1] + l[2] + l[3]
print(l)
print(reduce(counter, l))
