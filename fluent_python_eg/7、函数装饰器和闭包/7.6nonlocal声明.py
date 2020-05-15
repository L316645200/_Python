def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))


# 不用nonlocal解决
# def make_averager():
#     d = {
#         'count': 0,
#         'total': 0
#     }
#
#     def averager(new_value):
#         d['count'] += 1
#         d['total'] += new_value
#         return d['total'] / d['count']
#
#     return averager
#
# avg = make_averager()
# print(avg(10))
# print(avg(11))
# print(avg(12))