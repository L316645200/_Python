# 示例 8-3 charles 和 lewis 指代同一个对象
charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print(id(charles), id(lewis))
lewis['balance'] = 950
print(charles)
alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print( alex == charles)
print(alex is not charles)
# 示例 8-3 体现了别名。在那段代码中，lewis 和 charles 是别名，即 两个变量绑定同一个对象。
# 而 alex 不是 charles 的别名，因为二者绑 定的是不同的对象。alex 和 charles 绑定的对象具有相同的值（== 比 较的就是值），但是它们的标识不同。


# 8.2.2 元组的相对不可变性
"""元组与多数 Python 集合（列表、字典、集，等等）一样，保存的是对象 的引用。如果引用的元素是可变的，即便元组本身不可变，元素依然 可变。
也就是说，元组的不可变性其实是指 tuple 数据结构的物理内容（即保存的引用）不可变，与引用的对象无关。"""
# 示例 8-5 一开始，t1 和 t2 相等，但是修改 t1 中的一个可变元 素后，二者不相等了
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(t1 == t2)
print(id(t1[-1]))
t1[-1].append(99)
print(t1)
print(id(t1[-1]))
print(t1 == t2)

