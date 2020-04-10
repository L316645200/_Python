
storage_type = (('10', '容量型本地盘'),
                ('11', '容量型云盘'),
                ('20', '性能型本地盘'),
                ('21', '性能型云盘'),
                ('22', 'LVM云盘'))
# [{'value': 10, 'text': '容量型本地盘'}, {}, {}, {}, {}]

def example(a):
    return {'value': a[0], 'text': a[1]}


s = map(example, storage_type)
