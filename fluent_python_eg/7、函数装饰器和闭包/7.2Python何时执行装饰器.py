# 函数装饰器在导入模块时立即执行，而被装饰的 函数只在明确调用时运行。这突出了 Python 程序员所说的导入时和运 行时之间的区别。
registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()
# 函数装饰器在导入模块时立即执行，而被装饰的 函数只在明确调用时运行。这突出了 Python 程序员所说的导入时和运 行时之间的区别。
