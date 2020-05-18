# 定义 __slots__ 的方式是，创建一个类属性，使用 __slots__ 这个名 字，并把它的值设为一个字符串构成的可迭代对象，其中各个元素表示 各个实例属性。
# 我喜欢使用元组，因为这样定义的 __slots__ 中所含 的信息不会变化，如示例 9-11 所示。

# 示例 9-11 vector2d_v3_slots.py：只在 Vector2d 类中添加了 __slots__ 属性
import math
from array import array


class Vector2d:
    __slots__ = ('_x', '_y')

    typecode = 'd'

    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))
        # return bool(self.x or self.y)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self)
        return '({}, {})'.format(*components)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __complex__(self):
        return complex(self.x, self.y)
