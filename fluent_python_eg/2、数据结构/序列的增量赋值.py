from dis import dis

l = [1, 2, 3]
print(id(l))

l *= 2
print(l)
print(id(l))

t = (1, 2, 3)
print(id(t))
t *= 2
print(t)
print(id(t))


s = 'abc'
print(id(s))
s *= 3
print(s)
print(id(s))


t = (1, 2, [30, 40])
print(dis('t[2] += [50, 60]'))
# try:
#     t[2] += [50, 60]
#     # t[2]被改动了，但是也有异常抛出
#     # 这是因为t[2]指向列表[30, 40],[30, 40] += [50, 60]这一步可以完成
#     # 但是t[2] = [30, 40, 50, 60]赋值失败，s是不可变的元组
# # t[2].extend([50, 60])
# except Exception as e:
#     print(t)
