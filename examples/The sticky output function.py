funcs = []
results = []
for x in range(7):
    def some_func():
        return x
    funcs.append(some_func)
    results.append(some_func()) # 注意这里函数被执行了

funcs_results = [func() for func in funcs]

print(results)
print(funcs_results)

# 当在循环内部定义一个函数时, 如果该函数在其主体中使用了循环变量, 则闭包函数将与循环变量绑定, 而不是它的值.
# 因此, 所有的函数都是使用最后分配给变量的值来进行计算的.
# 可以通过将循环变量作为命名变量传递给函数来获得预期的结果. 为什么这样可行? 因为这会在函数内再次定义一个局部变量.
funcs = []
for x in range(7):
    def some_func(x=x):
        return x
    funcs.append(some_func)

funcs_results = [func() for func in funcs]
print(funcs_results)
