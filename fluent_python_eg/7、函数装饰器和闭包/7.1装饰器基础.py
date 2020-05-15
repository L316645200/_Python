# @decorate
# def target():
#     print('running target()')
#
# 上述代码的效果与下述写法一样
# def target():
#     print('running target()')
#
#
# target = decorate(target)


def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target()')


target()
