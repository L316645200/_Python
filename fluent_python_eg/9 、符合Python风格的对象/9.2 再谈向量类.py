# 示例 9-2 vector2d_v0.py：目前定义的都是特殊方法

import math
from array import array


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

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


# 示例 9-1 Vector2d 实例有多种表示形式

v1 = Vector2d(3, 4)
print(v1.x, v1.y)
x, y = v1
print(x, y)
print(v1)
v1_clone = eval(repr(v1))
print(v1 == v1_clone)
print(v1)

octets = bytes(v1)
print(octets)
print(abs(v1))
print(bool(v1), bool(Vector2d(0, 0)))

print(format(v1, '.3f'))


# c = (format(3.00, '0.3f'), format(4.00, '0.3f'))
# s = '({}, {})'.format(*c)
# print(s)