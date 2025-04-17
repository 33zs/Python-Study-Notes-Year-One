#map
"""
根据提供的函数对指定的序列做映射
map(function----函数,lterable-----序列)
返回一个迭代器，如果要转换成列表，可以用list（）转换
"""
#计算x的平方
def add(x):
    return x**2
lists=range(11)
a=map(add,lists)
print(a)#返回一个迭代器 <map object at 0x0000025574F68F70>
print(list(a))
#结果为：[0,1,4,.....]
#简洁
print(list(map(lambda x:x**2,range(11))))