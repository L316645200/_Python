# 示例 8-1 变量 a 和 b 引用同一个列表，而不是那个列表的副本
a = [1, 2, 3]
b = a
b.append(4)
print(b, a)


# 示例 8-2 创建对象之后才会把变量分配给对象
class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))

x = Gizmo()
# y = Gizmo* 10
print(dir())
