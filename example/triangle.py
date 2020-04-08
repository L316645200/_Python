# 杨辉三角

l = [1, 2, 3, 4, 5]
s = 10 + l[4] if len(l) >= 4 + 1 else 10
print(s)


def triangles(n):
    l = [[1] for i in range(n)]
    for i in range(1, n):
        for j in range(1, i + 1):
            l[i].append(l[i - 1][j - 1] + l[i - 1][j] if len(l[i - 1]) >= j + 1 else l[i - 1][j - 1])
    return l


for i in triangles(10):
    print(i)


def triangle(n):
    l = [1]
    m = 0
    while m < n:
        yield l
        l = [1] + [l[i] + l[i-1] for i in range(1, len(l))] + [1]
        m += 1


gen = triangle(10)

for i in gen:
    print(i)
