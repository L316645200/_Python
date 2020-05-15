"""接受函数为参数，或者把函数作为结果返回的函数是高阶函数（higher- order function）"""

# 示例5-3根据单词长度给一个列表排序

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))


# 示例 5-4 根据反向拼写给一个单词列表排序
def reverse(word):
    return word[::-1]


print(reverse('testing'))
print(sorted(fruits, key=reverse))

# 示例 5-5 计算阶乘列表：map 和 filter 与列表推导比较
from math import factorial

fact = factorial
print(list(map(fact, range(6))))
print([fact(n) for n in range(6)])
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2])