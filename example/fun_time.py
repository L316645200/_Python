import time


def func_time(func):
    def inner(*args, **kw):
        start_time = time.time()
        func(*args, **kw)
        end_time = time.time()
        print('函数运行时间为：', end_time - start_time, 's')

    return inner
