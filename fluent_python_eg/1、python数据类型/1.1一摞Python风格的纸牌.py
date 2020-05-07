import collections
from random import choice, shuffle

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


deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])
print(choice(deck))

# 判断扑克牌大小
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

print()
for card in sorted(deck, key=spades_high):  # doctest: +ELLIPSIS
    # print(card)
    pass

# 目前FrenchDeck不支持洗牌
# print(shuffle(deck))