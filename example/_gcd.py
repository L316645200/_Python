# # 最大公约数源码


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd(18, 24))
