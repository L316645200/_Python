
import collections
from random import shuffle

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    suits = 'spades diamonds clubs hearts'.split()  # 黑桃 方块 梅花 红心

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)  # 使类可以用len函数调用

    def __getitem__(self, position):  # 使类可迭代,且将[]操作交给了self._cards,使类支持切片操作
        return self._cards[position]


def set_card(deck, position, card):
    deck._cards[position] = card

FrenchDeck.__setitem__ = set_card
deck = FrenchDeck()
shuffle(deck)
for i in deck:
    print(i)