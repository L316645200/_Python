from bisect import bisect

fruits = ['grape', 'raspberry', 'apple', 'banana']

print(sorted(fruits))

print(fruits)

print(sorted(fruits, reverse=True))

print(sorted(fruits, key=len))

print(sorted(fruits, key=len, reverse=True))

fruits.sort()
print(fruits)


bisect