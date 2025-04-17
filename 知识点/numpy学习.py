import numpy as np
from scipy import stats
#numpy
#创建数组
'''
array(),所有元素为同一类型 中括号
'''
anArray=np.array([1,2,3,4])
print(anArray)
anArray1=np.array((1,2,3,4))
print(anArray1)
#ndim
'''
返回指示数组维数的整数
'''
An=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(An.ndim)
#访问元素
print(An[2][1])
print(An[2,1])
#各维度元素个数，数组元素个数
print(np.size(An,0))
print(An.size)
print("len",len(An))
#数组形状的乘积
#数组形状，返回元组
print("shape",np.shape(An))

#平均值Mean
l=np.array([10,20,30,40,50])
print(np.mean(l))
#中位数
print(np.median(l))
#众数(如果出现次数一样，返回值小的）
m=stats.mode(l)
print('mode=',m)
#求标准差
print(np.std(l))
#求百分位数
'''
1、从小到大排序数字
2、数字个数乘上百分数
  a、如果值是整数
  b、如果值非整数，则向上取整
3、百分位数是第二部值为索引所对应的数，第一个数字索引为1
'''
print(np.percentile(l,25))
#numpy.zeros(shape,dtype=float)
"""
shape：创建的新数组的形状（维度）
dtype:创建新数组的数据类型
返回值：给定维度的全零数组
"""
array2=np.zeros([2,3],dtype=np.int32)
print(array2)
print(array2.dtype)

#numpy.arange()
"""
np.arange([start,]stop,[step,]dtype=None)
start起始值，默认值为0
end 结束值（不含）
step步长(默认值为1)
dtype(默认为none)
"""
z=np.arange(6,10)
print(z)
print(np.arange(6,20,2))
print(type(z))
#nparray 是一个对象
#array 是一个方法

#numpy.random.seed()
"""
seed 用于指定随机数生成时所用算法开始的整数值
1、如果使用相同的seed()值，则每次生成的随机数相同
2、如果不设置这个值，则系统根据时间来选择这个值，因为时间不同而不同
3、设置的seed()值仅一次有效
"""
#numy shape
"""
当数组为一维时，返回数组内元素个数
"""
#参数是个数时返回为空
print(np.shape(0))
#参数是一维数组时
print(np.shape[1])
print(np.shape[1,2])
#参数是二维数组时
print(np.shape([1,1],[2,2],[3,3]))
#numpy.arange(n).reshape(a,b)
"""
依次生成n个自然数，并且以a行b列的数组形式显示
arr.reshape(m,-1)改变维度为m行，d列自动计算
arr.reshape(-1,m)改变维度为m列，d行自动计算
"""
print(np.arange(16).reshape(2,8))


