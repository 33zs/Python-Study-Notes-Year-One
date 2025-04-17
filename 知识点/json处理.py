#JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，
# 它具有简洁、清晰的层次结构，易于阅读和编写，还可以有效的提升网络传输效率。
# Python 标准库的 json 模块可以用来处理 JSON 格式数据的基本操作
#JSON语法规则
"""
1、名称必须用双引号（即：" "）来包括
2、值可以是双引号包括的字符串、数字、true、false、null、JavaScript数组，或子对象
3、数据在name/value中
4、数据见用逗号分隔
5、花括号保存对象
6、方括号保存数组
"""
#数据类型
"""
dict----object
list, tuple-----array
str, unicode-----string
int, long, float----number
True-----true
False-----false
None-----null
"""
#对象
"""
{"firstname": "jonh", "lastname": "Doe"}
"""
#数组
"""
包含三个对象的数组
{
	"employees": [
		{ “firstName”:“John” , “lastName”:“Doe” },
		{ “firstName”:“Anna” , “lastName”:“Smith” },
		{ “firstName”:“Peter” , “lastName”:“Jones” }
	]
}
"""
#常用方法
"""
python在使用json这个模块前，首先要导入json库：import json.
方法	描述
json.dumps()	将 Python 对象编码成 JSON 字符串
json.loads()	将已编码的 JSON 字符串解码为 Python 对象
json.dump()	将Python内置类型序列化为json对象后写入文件
json.load()	读取文件中json形式的字符串元素转化为Python类型
注意：不带s的是序列化到文件或者从文件反序列化，带s的都是内存操作不涉及持久化。
"""
#json.dumps()
import json

data = {'name': 'nanbei', 'age': 18}
# 将Python对象编码成json字符串
print(json.dumps(data))

#将单引号变为双引号了

#json.loads()
import json

data = {'name': 'nanbei', 'age': 18}
# 将Python对象编码成json字符串
# print(json.dumps(data))
# 将json字符串解码成Python对象
a = json.dumps(data)
print(json.loads(a))

import json

data = (1, 2, 3, 4)
data_json = [1, 2, 3, 4]
# 将Python对象编码成json字符串
print(json.dumps(data))
print(json.dumps(data_json))

# 将Python对象编码成json字符串
a = json.dumps(data)
b = json.dumps(data_json)
# 将json字符串编码成Python对象
print(json.loads(a))
print(json.loads(b))
#结果
"""
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
元组和列表解析出来均是数组，
解码后，json的数组最终被转化成python的list，无论原来是list还是tuple
"""
#json.dump()
#将python序列化为json对象后写入文件
"""
import json
 
data = {
    'nanbei':'haha',
    'a':[1,2,3,4],
    'b':(1,2,3)
}
with open('json_test.txt','w+') as f:
    json.dump(data,f)
"""
#json.load()
#读取文件中json元素转为python类型
"""
import json
 
data = {
    'nanbei':'haha',
    'a':[1,2,3,4],
    'b':(1,2,3)
}
with open('json_test.txt','w+') as f:
    json.dump(data,f)
 
with open('json_test.txt','r+') as f:
    print(json.load(f))
"""
#结果
#{'a': [1, 2, 3, 4], 'b': [1, 2, 3], 'nanbei': 'haha'}
#类型转化
#python的列表转换为json的数组
import json
print(json.dumps([1,2,3]))
'[1, 2, 3]'
#python的字符串转换为json的字符串
print(json.dumps('abdcs'))
'"abdcs"'
#python的元祖转换为json的数组
print(json.dumps((1,2,3,'a')))
'[1, 2, 3, "a"]'#注意此时显示的是方括号
#python的字典转换为json的对象
print(json.dumps({1:'a',2:'b'}))
'{"1": "a", "2": "b"}'#注意此时1和2转换后是加了引号的，因为json的名称是必须要加引号的
#python的整数转换为json的数字
print(json.dumps(13))
'13'
#python的浮点数转换为json的数字
print(json.dumps(3.1415))
'3.1415'
#python的unicode字符串转换为json的字符串
print(json.dumps(u'a'))
'"a"'
#python的True转换为json的数组true
print(json.dumps(True))
'true'
#python的False转换为json的数组false
print(json.dumps(False))
'false'
#python的None转换为json的null
print(json.dumps(None))
'null'
#json本质上是一个字符串
print(type(json.dumps('abc')))
"<class 'str'>"
#dumps/dumps
"""
import json

# dumps可以格式化所有的基本数据类型为字符串
data1 = json.dumps([])         # 列表
print(data1, type(data1))
data2 = json.dumps(2)          # 数字
print(data2, type(data2))
data3 = json.dumps('3')        # 字符串
print(data3, type(data3))
dict = {"name": "Tom", "age": 23}   # 字典
data4 = json.dumps(dict)
print(data4, type(data4))

with open("test.json", "w", encoding='utf-8') as f:
    # indent 超级好用，格式化保存字典，默认为None，小于0为零个空格
    f.write(json.dumps(dict, indent=4))
    json.dump(dict, f, indent=4)  # 传入文件描述符，和dumps一样的结果
"""
#输出
"""
[] <class 'str'>
2 <class 'str'>
"3" <class 'str'>
{"name": "Tom", "age": 23} <class 'str'>
test.py
{
    "name": "Tom",
    "age": 23
}
"""
#load/loads
"""
import json

dict = '{"name": "Tom", "age": 23}'   # 将字符串还原为dict
data1 = json.loads(dict)
print(data1, type(data1))

with open("test.json", "r", encoding='utf-8') as f:
    data2 = json.loads(f.read())    # load的传入参数为字符串类型
    print(data2, type(data2))
    f.seek(0)                       # 将文件游标移动到文件开头位置
    data3 = json.load(f)
    print(data3, type(data3))
"""
#输出
"""
{'name': 'Tom', 'age': 23} <class 'dict'>
{'name': 'Tom', 'age': 23} <class 'dict'>
{'name': 'Tom', 'age': 23} <class 'dict'>
"""
#dumps参数详解
"""
dumps(obj,skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw):
函数作用: 将Python对象转变成JSON对象，便于序列化内存/文件中。

参数：

skipkeys: 如果为True的话，则只能是字典对象，否则会TypeError错误, 默认False
ensure_ascii: 确定是否为ASCII编码
check_circular: 循环类型检查，如果为True的话
allow_nan: 确定是否为允许的值
indent: 会以美观的方式来打印，呈现，实现缩进
separators: 对象分隔符，默认为,
encoding: 编码方式，默认为utf-8
sort_keys: 如果是字典对象，选择True的话，会按照键的ASCII码来排序
"""
#dump(多一个fp参数，保存文件对象)
"""
dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw)

Serialize ``obj`` as a JSON formatted stream to ``fp`` (a``.write()``-supporting file-like object).
"""
#总结
"""

json.dumps 将 Python 对象编码成 JSON 字符串
json.loads 将已编码的 JSON 字符串解码为 Python 对象
json.dump和json.load，需要传入文件描述符，加上文件操作。
json内部的格式要注意，一个好的格式能够方便读取，可以用indent格式化。

个人总结：

dump：存入的实例对象object（序列化）

dumps：存入的JSON的字符串数据

load：读取的实例对象object（反序列化）

loads：读取的JSON的字符串数据，转化为Python字典对象
"""