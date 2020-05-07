a = b = [1, 2, 3]
a.append(4)
print(a, b)
print('----------')

str1 = 'hello\b'  # \转义  \b退格
print(str1)
print('----------')

a = False
b = 100
print(a and b)
print(a or b)
print('----------')

str2 = 'bell'
# str2[1] = 'a'  # 字符串不可变
print('----------')

str3 = 'Hello World!'
print(str3.split())
print('----------')

# print(6+4j>3-2j)

# list = [a, b, c]  # list为列表函数
# list.append(d) + list(123)


string = 'my name is x'
for i in string:
    print(i, end=",")