# 题目：已知 sqrt (2)约等于 1.414，要求不用数学库，求 sqrt (2)精确到小数点后 10 位

up = 1.415
down = 1.414
target = (up + down) / 2
EPSILON = 0.1 ** 10
while up - down >= EPSILON:
    if target ** 2 > 2:
        up = target
    else:
        down = target
    target = (up + down) / 2
print(target)
print("%2.10f" % target)

# 牛顿迭代法
# 1.牛顿迭代法的公式为：
# xn+1 = xn-f(xn)/f'(xn)

# 对于本题，需要求解的问题为：f(x)=x2-2 的零点
EPSILON = 0.1 ** 10


def newton(x):
    if abs(x ** 2 - 2) > EPSILON:
        return newton(x - (x ** 2 - 2) / (2 * x))
    else:
        return x



print(newton(2))

