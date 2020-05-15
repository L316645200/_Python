# WeakValueDictionary 类实现的是一种可变映射，里面的值是对象的 弱引用。
# 被引用的对象在程序中的其他地方被当作垃圾回收后，对应的 键会自动从 WeakValueDictionary 中删除。
# 因 此，WeakValueDictionary 经常用于缓存。

# 示例 8-18 实现一个简单的类，表示各种奶酪。 示例 8-18 Cheese 有个 kind 属性和标准的字符串表示形式


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

# 在示例 8-19 中，我们把 catalog 中的各种奶酪载入 WeakValueDictionary 实现的 stock 中。
# 然而，删除 catalog 后，stock 中只剩下一种奶酪了。你知道为什么帕尔马干酪 （Parmesan）比其他奶酪保存的时间长吗？ 代码后面的提示中有答 案

# 示例 8-19 顾客：“你们店里到底有没有奶酪？”


import weakref
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
           Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys()))
del cheese
print(sorted(stock.keys()))










