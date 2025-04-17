import copy
#字典
#创建方式
#1
dict1={'1':1}
#2
lst=[('age',99),('time',22)]
dict2=dict(lst)
print(dict2)
#3
dict3=dict(age=99,time=22)
print(dict3)
#4
list1=['age','time']
list2=[99,22]
dict4=dict(zip(list1,list2))
print(dict4)

#dict.clear()
'''
清空字典中的键值对，变为一个空字典
'''
print(dict4.clear())

#copy()
dict9={'age':[18,99],'sex':'man'}
dict5=dict9 #浅拷贝 引用对象
dict6=dict9.copy() #浅拷贝：深拷贝父对象，子对象引用
#dict7=dict9.copy.deepcopy(dict9)
dict9['age'].remove(18)
dict9['age']=20
#dict9={'age':20,'sex':'man'}
#dict5={'age':20,'sex':'man'}
#dict6={'age':[99],'sex':'man'}
#dict7={'age':[18,99],'sex':'man'}

#dict.fromkeys()
'''
使用给定的多个键创建一个新字典，值默认都是None，
也可以传入一个参数作为默认值
'''
list3=['age','sex']
dict10=dict.fromkeys(list3)
dict11=dict.fromkeys(list3,'python')
print(dict10)
print(dict11)

#dict.get()
'''
get()返回指定键的值，根据键来获得值，
在键不存在的情况下，返回None,
也可以指定返回值
'''
age=dict11.get('age')
print(age)
phone=dict11.get('phone')
print(phone)
phone=dict11.get('phone','123455')
print(phone)

#dict.items()获得字典的键值对
items=dict11.items()
print(items)
print(type(items))
print(list(items))
#dict.keys 获得字典的所有键
keys=dict11.keys()
print(keys)
print(type(keys))
print(list(keys))
#dict.values() 返回一个字典所有的值
values=dict11.values()
print(values)
print(type(values))
print(list(values))
#dict.pop(key)
''''
 返回指定键对应的值，并在原字典中删除这个键值对
'''
dict12={'sex':'男','age':99}
sex=dict12.pop('sex')
print('sex=',sex)
print(dict12)
#dict,popitem()
'''
删除字典中的最后一对键值对
'''
dict13={'1':1,'2':2}
dict13.popitem()
print(dict13)
#dict.setdefault()
'''
和get()类似，
如果键不存在于字典中，则添加键并将值设为default
'''
a={'1':1,'2':2}
print(a.setdefault('1'))
print(a.setdefault('3',3))
print(a)
'''
1
3
{'1': 1, '2': 2, '3': 3}
'''
#dict.update(dict1)
'''
字典更新，将字典dict1的键值对更新到dict
如果已经包含对于的键值对，原键值对会被覆盖，
如果更新的字典不包含该键值对，则添加该键值对
'''
b={'3':4,'4':4}
a.update(b)
print(a)

#in 判断的是key
#len()
print(len(b))

#构造字典
a=dict(one=1,two=2,three=3)
b={"one":1,"two":2,"three":3}
c=dict(zip(["one","two","three"],[1,2,3]))
d=dict([("two",2),("one",1),("three",3)])
e=dict({"three":3,"one":1,"two":2})
a==b==c==d==e

#list(d)
"返回字典的所有键"
print(list(b))

#key in d
"返回True如果key存在"

#iter(d)
"迭代所有键"

#reversed(d)
"逆序所有键"

#怎样避免keyerror
#1、用key in dict
if "one" in d:
    print(d["one"])
else:
    print("not in map")

#2、用dict.get(key)，返回None如果不存在
d.get("one")
d.get("222")
"""
可以用来作为判断条件
if dict.get("d")==None:
"""

#dict排序
"""
sorted(iterable, key=None, reverse=False)
参数说明：

 - iterable -- 可迭代对象。 
 - key --主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。 
 - reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

返回：
 - 一个新list对象  
"""
from operator import itemgetter
dict = {3: 'B', 1: 'A', 2: 'C'}

# 按key升序
# 1. dict.items()取得3个(key,value)
# 2. lambda x: x[0]取(key,value)的key   即(3,1,2)
d1 = sorted(dict.items(), key=lambda x: x[0], reverse=False)  # <class 'list'>

# 按key降序   itemgetter类似lambda
d2 = sorted(dict.items(), key=itemgetter(0), reverse=True)  # <class 'list'>

# 输出
print(d1, type(d1))  # [(1, 'A'), (2, 'C'), (3, 'B')] <class 'list'>
print(d2, type(d2))  # [(3, 'B'), (2, 'C'), (1, 'A')] <class 'list'>

from operator import itemgetter
dict = {3: 'B', 1: 'A', 2: 'C'}

# 按value升序
# 1. dict.items()取得3个(key,value)
# 2. lambda x: x[1]取(key,value)的value   即('B','A','C')

d3 = sorted(dict.items(), key=lambda x: x[1], reverse=False)  # <class 'list'>

# 按value降序   itemgetter类似lambda
d4 = sorted(dict.items(), key=itemgetter(1), reverse=True)  # <class 'list'>

print(d3, type(d3))  # [(1, 'A'), (3, 'B'), (2, 'C')] <class 'list'>
print(d4, type(d4))  # [(2, 'C'), (3, 'B'), (1, 'A')] <class 'list'>

dict = {4:'B', 3: 'B', 1: 'A', 2: 'C', 5: 'A'}

# 按value进行升序，value相同再按key进行降序
d3 = sorted(dict.items(), key=lambda x: (x[1] , -x[0]), reverse=False)
print(d3, type(d3))  # [(5, 'A'), (1, 'A'), (4, 'B'), (3, 'B'), (2, 'C')] <class 'list'>

# 按value进行降序，value相同再按key进行升序
d3 = sorted(dict.items(), key=lambda x: (-ord(x[1]) , x[0]), reverse=False)  # 对字符降序比较可以先转ord。如果是'123'字符串数字可以使用int，其他规则请自行延伸。
print(d3, type(d3))  # [(2, 'C'), (3, 'B'), (4, 'B'), (1, 'A'), (5, 'A')] <class 'list'>
