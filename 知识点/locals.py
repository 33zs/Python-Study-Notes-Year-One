#locals() 函数访问到局部名字空间
def func(a):
    b = a
    print(locals())
func(3)

#**locals() 将根据 formatStr 中位于括号内的变量名实现映射解包操作。
def fun(a, b):
    x = 20
    y = 30
    sum = x + y
    prod = x * y
    formatStr = '{x} + {y} = {sum}; {x} * {y} = {prod}.'
    print(formatStr.format(**locals()))

# print: '20 + 30 = 50; 20 * 30 = 600.'