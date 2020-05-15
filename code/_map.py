
storage_type = (('10', '容量型本地盘'),
                ('11', '容量型云盘'),
                ('20', '性能型本地盘'),
                ('21', '性能型云盘'),
                ('22', 'LVM云盘'))
# [{'value': 10, 'text': '容量型本地盘'}, {}, {}, {}, {}]

def example(a):
    return {'value': a[0], 'text': a[1]}


s = map(example, storage_type)
for i in s:
    print(i)

def add(x, y):
    return x + y

s = [1, 2, 3, 4, 5]
m = map(add, s, s)
for i in m:
    print(i)


def examples(storage_type):
    for a in storage_type:
        yield {'value': a[0], 'text': a[1]}


print(examples(storage_type))


# 自己写map
def my_map(func, lst):
    map_list = []

    for l in lst:
        map_list.append(func(l))

    return map_list

s = [1, 2, 3, 4, 5]
m = my_map(add, s, s)
for i in m:
    print(i)

# 自己写filter
def my_filter(func, lst):
    filter_list = []

    for l in lst:
        if func(l):
            filter_list.append(l)

    return filter_list
