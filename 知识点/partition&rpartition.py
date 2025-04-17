"""
partition(str) & rpartition(str)
这2个函数的功能一样都是用来将完整的字符串以某个子串分割成三段，分别是子串前，子串和子串后，返回值是一个包含三段字符串的列表，下面来看下具体用法：

用途：
partition(str) 函数以str对完整字符串进行分割，str为从字符串**左侧**开始匹配到的第一个字符串
rpartition(str) 函数以str对完整字符串从右侧开始进行分割，str为从字符串**右侧**开始匹配到的第一个字符串
语法：partition(str)/rpartition(str)
用法：xxx.partition(str)/xxx.rpartition(str)
其中，xxx代表的是一个完整的字符串，self参数不用传递，str要进行字符串分割的子串，可以是空格但不能为空字符串
"""
mystr = 'hello wrold and hello python'
mystr.partition('and')

#输出结果
#['hello world','and','hello python']

mystr = 'hello python and python hello'

mystr.rpartition('python')

#输出结果
#['hello python and','python','hello']
