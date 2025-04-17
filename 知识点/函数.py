#函数
#1 缺省参数
'''
在形参中默认有值的参数为缺省参数
调用函数，缺省参数的值如果没有传入，则取默认值
带有默认值的参数一定要位于参数列表的最后面
'''
def sum1(a,b=9):
    print(a+b)
sum1(a=2)
sum1(a=2,b=8)
#2 不定长参数
'''
加了星号（*）的变量args会存放所有未命名的变量参数，args为元组
加了**的变量的kwargs会存放命名参数，形如key=value,kwargs为字典
'''
def sum(a,b,*args,c=1,e=2,**kwargs):
    print(a)
    print(b)
    print(args)
    for key,value in kwargs.items():
        print(value)
        print(key)
    print(c)
    print(e)
sum(1,2,3,4,5,6,7,n=1,m=2,p=3)
#缺省参数在*args后面，kwargs一定在最后
#函数返回值
'''
程序中函数完成一件事情后，最后给调用者的结果
多个return语句，只要有一个return语句被执行到，那么函数就会结束，后面的return不执行
return 能够存储多个数据的类型，例如元组，列表，字典
'''
def add(a,b):
    return a+b
result=add(1,1)
print('result',result)
def add2(a,b):
    c=a+b
print(add2(1,1))
#局部变量
'''
在函数内定义的变量
临时保存数据需要在函数中定义变量来进行储存
当函数被调用完成，变量不能再用
'''
#全局变量（在函数外定义的） 能够再所有的函数进行访问
#1 全局变量与局部变量名字相同,定义局部变量
a=100
def test1():
    a=300
    print(a)
    a=200
    print(a)
def test2():
    print(a)
test1()
test2()
#2修改全局变量
'''
用global声明
'''
def test3():
    global a
    print(a)
    a=200
    print(a)
test3()
test2()
#拆包
def f():
    height=11
    weight=22
    age=18
    return height,weight,age
result=f()
print(result)
my_high,my_weight,my_age=f()
print(my_high)
print(my_weight)
print(my_age)
#python中函数参数是引用传递
