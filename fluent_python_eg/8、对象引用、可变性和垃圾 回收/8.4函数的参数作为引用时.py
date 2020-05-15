# 示例 8-11 函数可能会修改接收到的任何可变对象


def f(a, b):
    a += b
    return a


x = 1
y = 2
print(f(x, y))
print(x, y)

a = [1, 2]
b = [3, 4]
print(f(a, b))
print(a, b)

t = (10, 20)
u = (30, 40)
print(f(t, u))
print(t, u)


# 8.4.1 不要使用可变类型作为参数的默认值


class HauntedBus:
    """备受幽灵乘客折磨的校车"""

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


print()
# HauntedBus 的诡异行为
# 示例 8-13 备受幽灵乘客折磨的校车
bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)

print()
bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)

print()
bus3 = HauntedBus()
print(bus3.passengers)
bus3.pick('Dave')
print(bus2.passengers)
print(bus2.passengers is bus3.passengers)
print(bus1.passengers)
"""实例化 HauntedBus 时，如果 传入乘客，会按预期运作。
但是不为 HauntedBus 指定乘客的话，奇怪 的事就发生了，这是因为 self.passengers 变成了 passengers 参数 默认值的别名。
出现这个问题的根源是，默认值在定义函数时计算（通 常在加载模块时），因此默认值变成了函数对象的属性。
因此，如果默 认值是可变对象，而且修改了它的值，那么后续的函数调用都会受到影 响。"""


# 8.4.2 防御可变参数

# 示例 8-15 一个简单的类，说明接受可变参数的风险
class TwilightBus:
    """让乘客销声匿迹的校车"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


# 示例 8-14 从 TwilightBus 下车后，乘客消失了
basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team)

"""这里的问题是，校车为传给构造方法的列表创建了别名。
正确的做法 是，校车自己维护乘客列表。
修正的方法很简单：在 __init__ 中，传 入 passengers 参数时，
应该把参数值的副本赋值给 self.passengers = list(passengers)"""

"""创建 passengers 列表的副本；如果不是列表，就把它转换成列 表。
在内部像这样处理乘客列表，就不会影响初始化校车时传入的参数了。 
此外，这种处理方式还更灵活：现在，传给 passengers 参数的值可以 是元组或任何其他可迭代对象，
例如 set 对象，甚至数据库查询结果， 因为 list 构造方法接受任何可迭代对象。
自己创建并管理列表可以确 保支持所需的 .remove() 和 .append() 操作，这样 .pick() 和.drop() 方法才能正常运作。"""