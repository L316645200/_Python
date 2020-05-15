import time
from example.fun_time import func_time

# 斐波那契
# 递归
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# 动态规划
@func_time
def dp_fib(n):
    results = [0 for _ in range(n + 1)]

    for i in range(n + 1):
        if i < 2:
            results[i] = i
        else:
            results[i] = results[i - 1] + results[i - 2]

    return results[1:]


start_time = time.time()
fib(30)
end_time = time.time()
print('函数运行时间为：', end_time - start_time, 's')
dp_fib(10000)

# 递归通过前两个值推出当前值，继续去推前两个值，虽然简单易懂，但是递归的方式造成栈空间的极大浪费，而且该算法的时间复杂度O(2^n)

# 动态规划通过保存前两个值，得出后面的值,算法时间复杂度为O(n)




