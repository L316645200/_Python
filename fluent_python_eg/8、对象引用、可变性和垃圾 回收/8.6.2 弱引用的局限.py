# 不是每个 Python 对象都可以作为弱引用的目标（或称所指对象）。
# 基本 的 list 和 dict 实例不能作为所指对象，但是它们的子类可以轻松地 解决这个问题：
import weakref


class MyList(list):
    """list的子类，实例可以作为弱引用的目标"""


a_list = MyList(range(10))
# a_list可以作为弱引用的目标
wref_to_a_list = weakref.ref(a_list)
