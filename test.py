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


