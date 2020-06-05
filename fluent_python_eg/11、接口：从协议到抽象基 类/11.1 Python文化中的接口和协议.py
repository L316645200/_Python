# 示例 11-1 vector2d_v0.py：x 和 y 是公开数据属性
class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)

        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))
    # 下面是其他方法（这个代码清单将其省略了）
