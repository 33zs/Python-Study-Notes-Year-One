# course='JC1001'
# course_iter=iter(course)
# print(next(course_iter))
# print(next(course_iter))
# print(next(course_iter))
# print(next(course_iter))
# print(next(course_iter))
# print(next(course_iter))
# print(next(course_iter))#没有元素则出错


"""
可迭代对象需具有 __iter__() 方法，它们均可使用 for 循环遍历，
可以使用 isinstance() 方法来判断一个对象是否为可迭代对象，
"""

# # from collections import Iterable
#
# print(isinstance('abc', Iterable))
# print(isinstance({1, 2, 3}, Iterable))
# print(isinstance(1024, Iterable))
"""
迭代器需要具有 __iter__() 和 __next__() 两个方法
__iter__()：返回迭代器对象本身
__next__()：返回下一项数据
"""

class MyIterator:
    def __init__(self):
        self.s = '程序之间'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < 4:
            n = self.s[self.i]
            self.i += 1
            return n
        else:
            raise StopIteration

mi = iter(MyIterator())
for i in mi:
    print(i)
#生成器是用来创建迭代器的工具
"""
yield 是一个关键字，作用和 return 差不多，
差别在于 yield 返回的是一个生成器（在 Python 中，一边循环一边计算的机制，称为生成器），
它的作用是：有利于减小服务器资源，在列表中所有数据存入内存，而生成器相当于一种方法而不是具体的信息，用多少取多少，占用内存小。

使用 yield 语句、
生成器表达式（可以简单的理解为是将列表的 [] 换成了 ()。
"""
def reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]
for char in reverse('Hello'):
    print(char)

# 列表
lis = [x*x for x in range(5)]
print(lis)

# 生成器
gen = (x*x for x in range(5))
for g in gen:
    print(g)