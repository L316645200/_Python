# 示例 8-16 没有指向对象的引用时，监视对象生命结束时的情形
import weakref

s1 = {1, 2, 3}
s2 = s1


def bye():
    print('Gone with the wind...')


ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1
print(ender.alive)
s2 = 'spam'
print(ender.alive)
# s1 和 s2 是别名，指向同一个集合，{1, 2, 3}。  这个函数一定不能是要销毁的对象的绑定方法，否则会有一个指向 对象的引用。
# 在 s1 引用的对象上注册 bye 回调。 调用 finalize 对象之前，.alive 属性的值为 True。
# 如前所述，del 不删除对象，而是删除对象的引用。 重新绑定最后一个引用 s2，让 {1, 2, 3} 无法获取。
# 对象被销毁 了，调用了 bye 回调，ender.alive 的值变成了 False。
# 示例 8-16 的目的是明确指出 del 不会删除对象，但是执行 del 操作后 可能会导致对象不可获取，从而被删除。
# 你可能觉得奇怪，为什么示例 8-16 中的 {1, 2, 3} 对象被销毁了？毕 竟，我们把 s1 引用传给 finalize 函数了，而为了监控对象和调用回
# 调，必须要有引用。这是因为，finalize 持有 {1, 2, 3} 的弱引 用，
