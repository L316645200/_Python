# 示例 11-9 tombola.py：Tombola 是抽象基类，有两个抽象方法和 两个具体方法
import abc


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素。"""

    @abc.abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回。 如果实例为空，这个方法应该抛出`LookupError`。
        """

    def loaded(self):
        """如果至少有一个元素，返回`True`，否则返回`False`。"""
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元组，由当前元素构成。"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


# 示例 11-12 bingo.py：BingoCage 是 Tombola 的具体子类
import random


class BingoCage(Tombola):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()


# 示例 11-13 lotto.py：LotteryBlower 是 Tombola 的具体子类， 覆盖了继承的 inspect 和 loaded 方法
class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))
