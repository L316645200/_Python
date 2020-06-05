import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()  # 使bingo()成为bingo.pick()的快捷方式


bingo = BingoCage(range(3))
print(bingo.pick())
# print(bingo.pick())
print(bingo())
