# 示例 7-8 average_oo.py：计算移动平均值的类
class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))


# 示例 7-9 average.py：计算移动平均值的高阶函数


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return averager

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))

