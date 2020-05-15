# 7.8.1 使用functools.lru_cache做备忘
# 示例 7-18 生成第 n 个斐波纳契数，递归方式非常耗时
import functools
import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(30))

# lru_cache 可以使用两个可选的参数来配置。它的签名 是
# functools.lru_cache(maxsize=128, typed=False)
# maxsize 参数指定存储多少个调用的结果。缓存满了之后，旧的结果会 被扔掉，腾出空间。
# 为了得到最佳性能，maxsize 应该设为 2 的 幂。
# typed 参数如果设为 True，把不同参数类型得到的结果分开保存，即把通常认为相等的浮点数和整数参数（如 1 和 1.0）区分开。
# 顺便说一下，因为 lru_cache 使用字典存储结果，而且键根据调用时传入的定位参数和关键字参数创建，
# 所以被lru_cache 装饰的函数，它的所有参数都必须是可散列的

# 7.8.2 单分派泛函数
print()
import html


def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)
print(htmlize({1, 2, 3}))
