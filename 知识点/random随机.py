import random
import numpy as np
#一、随机整数：
"""
1、包含上下限:[a,b]
random.randint(a,b)
"""
print(random.randint(1,50))

"""
2、不包含上下限：[a,b)
random.randrange(a,b)
random.randrange(a,b,c)
"""
print(random.randrange(1,50))
print(random.randrange(10,100,2))
#相当于从[10,12,14....]取随机数
"""
两者区别：
1、
randint 可以取左右极限
randrange只可以取左
2、
randrange 可以设置步长
randint 不可以设置步长
"""
#二、随机浮点数：
"""
1、0-1之间的随机浮点数
random.random
"""
print(random.random)
"""
2、随机浮点数
random.uniform(a,b)
可以允许，下限大于上限，可以等于上下限
"""
#三、随机选取字符
"""
1、随机字符
random.choice(sequence)
从序列中随机选取一个元素
"""
print(random.choice("abdsddafsaaf"))
print(random.choice("学习python"))
print(random.choice(["jsda","is","a"]))
print(random.choice(("tuple","is","a")))
#numpy.random
#1 numpy.random.random_sample([size])
"""
返回随机的浮点数，在半开区间[0.0,1,0]
"""
a=np.random.random_sample(4)
print(a)
#2 numpy.random.rand()
"""
随机值,矩阵表示
"""
print(np.random.rand(3,2))

