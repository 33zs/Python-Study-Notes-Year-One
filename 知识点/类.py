#__init__()function
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sayName(self):
        print('i am '+self.name)
cat1=Cat('cat1',10)

print(cat1.name)
print(cat1.age)

cat1.sayName()
#修改属性
cat1.name='baby'
print(cat1.name)
cat1.sayName()
#删除属性
'''
del cat1.age
print(cat1.age)
'''
#del cat1 删除实例
#继承
class cidy(Cat):
    def __init__(self,name):
        Cat.__init__(self,name,22)
cat2=cidy('cat2')
print(cat2.age)
#封装
'''
封装方法:__func
封装属性:__attr
'''
class student(object):
    def __init__(self,name,age):
        self.__name = name   # 封装的属性
        self.__age = age

    def __name_age(self):  # 封装方法
        return "name: %s; age: %s"%(self.__name,self.__age)

    def get_name_age(self):
        return self.__name_age()

jmz = student('jmz',13)
# print(jmz.__name)   #会报错AttributeError: 'student' object has no attribute '__name'
print(jmz.get_name_age())


'''
输出结果
name: jmz; age: 13
'''
#在封装属性前加_类名可以打印出封装的属性
print(jmz._student__name)
'''
输出结果
jmz
'''
#repr/str
"""
1.除了字符串类型外，使用str还是repr转换没有什么区别，字符串类型的话，外层会多一对引号，这一特性有时候在eval操作时特别有用；

2.命令行下直接输出对象调用的是对象的repr方法，print输出调用的是str方法
"""

#__new__()
class Person(object):

    def __new__(cls):
        print("__new__ called")
        return super().__new__(cls)

    def __init__(self):
        print("__init__ called")


a = Person()


