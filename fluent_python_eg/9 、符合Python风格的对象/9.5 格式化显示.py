brl = 1/2.43
print(brl)
print(format(brl, '0.4f'))
print('1 BRL = {rate:0.2f} USD'.format(rate=brl))


# 格式规范微语言为一些内置类型提供了专用的表示代码。
# 比如，b 和 x 分别表示二进制和十六进制的 int 类型，f 表示小数形式的 float 类 型，而 % 表示百分数形式
print(format(42, 'b'))
print(format(2/3, '.1%'))


# 格式规范微语言是可扩展的，因为各个类可以自行决定如何解释 format_spec 参数。
# 例如， datetime 模块中的类，它们的 __format__ 方法使用的格式代码与 strftime() 函数一样。
# 下面是内 置的 format() 函数和 str.format() 方法的几个示例：
from datetime import datetime
now = datetime.now()
print(now)
print(format(now, '%H:%M:%S'))
print("It's now {:%I:%M %p}".format(now))
