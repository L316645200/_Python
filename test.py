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


print()
print()
print()

l = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]

for i in l:
    i[:0] = ['0']
    i.append('0')
l[:0] = [['0'] * len(l[0])]
l.append(['0'] * len(l[0]))

for i in l:
    print(i)