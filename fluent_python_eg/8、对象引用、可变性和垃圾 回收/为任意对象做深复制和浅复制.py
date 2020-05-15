# 示例 8-8 校车乘客在途中上车和下车


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

# 示例 8-9 使用 copy 和 deepcopy 产生的影响
import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))

bus1.drop('Bill')
print(bus2.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
print(bus3.passengers)

print()
# 示例 8-10 循环引用：b 引用 a，然后追加到 a 中；deepcopy 会 想办法复制 a
a = [10, 20]
b = [a, 30]

a.append(b)

print(a)
c = copy.deepcopy(a)
print(c)